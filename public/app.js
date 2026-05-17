document.addEventListener('DOMContentLoaded', () => {
    const analyzeBtn = document.getElementById('analyze-btn');
    const usernameInput = document.getElementById('username');
    
    const loadingEl = document.getElementById('loading');
    const resultsEl = document.getElementById('results');
    const errorEl = document.getElementById('error');
    const errorMessageEl = document.getElementById('error-message');

    // Make sure 'marked' is loaded for markdown parsing
    const renderMarkdown = window.marked ? window.marked.parse : text => `<p>${text}</p>`;

    analyzeBtn.addEventListener('click', analyzeProfile);
    usernameInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') analyzeProfile();
    });

    async function analyzeProfile() {
        const username = usernameInput.value.trim();
        if (!username) return;

        // Reset UI
        errorEl.classList.add('hidden');
        resultsEl.classList.add('hidden');
        loadingEl.classList.remove('hidden');

        try {
            const response = await fetch(`/api/analyze?user=${encodeURIComponent(username)}`);
            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.detail || 'Failed to fetch profile');
            }

            renderProfile(data.profile);
            renderInsights(data.insights);
            
            loadingEl.classList.add('hidden');
            resultsEl.classList.remove('hidden');
        } catch (error) {
            loadingEl.classList.add('hidden');
            errorMessageEl.textContent = error.message;
            errorEl.classList.remove('hidden');
        }
    }

    function renderProfile(profile) {
        document.getElementById('r-name').textContent = profile.name || profile.username;
        document.getElementById('r-username').textContent = `@${profile.username}`;
        document.getElementById('r-bio').textContent = profile.bio || 'No bio provided';
        
        document.getElementById('r-repos').textContent = profile.public_repos;
        document.getElementById('r-followers').textContent = profile.followers;
        document.getElementById('r-stars').textContent = profile.total_stars;

        // Render languages
        const langsContainer = document.getElementById('r-languages');
        langsContainer.innerHTML = '';
        Object.entries(profile.top_languages).slice(0, 5).forEach(([lang, count]) => {
            const span = document.createElement('span');
            span.className = 'tag';
            span.textContent = `${lang} (${count})`;
            langsContainer.appendChild(span);
        });

        // Render Repos
        const reposContainer = document.getElementById('r-repos-list');
        reposContainer.innerHTML = '';
        profile.repos.forEach(repo => {
            const card = document.createElement('div');
            card.className = 'repo-card';
            card.innerHTML = `
                <h3><a href="${repo.url}" target="_blank">${repo.name}</a></h3>
                <p>${repo.description || 'No description'}</p>
                <div class="repo-footer">
                    <span><span style="color:var(--accent)">●</span> ${repo.language || 'N/A'}</span>
                    <span>⭐ ${repo.stars}</span>
                </div>
            `;
            reposContainer.appendChild(card);
        });
    }

    function renderInsights(insights) {
        // Use marked.js to convert the markdown response to HTML
        document.getElementById('r-ai-insights').innerHTML = renderMarkdown(insights);
    }
});
