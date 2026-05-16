import argparse
import sys
from github_api import get_summary_data
from ai_analyzer import analyze_profile
from report import print_report, save_report


def main():
    parser = argparse.ArgumentParser(
        description="🔍 GitHub Profile Analyzer — AI-powered developer insights"
    )
    parser.add_argument(
        "--user",
        type=str,
        required=True,
        help="GitHub username to analyze (e.g. --user torvalds)"
    )
    parser.add_argument(
        "--save",
        action="store_true",
        help="Save the report as a Markdown file"
    )

    args = parser.parse_args()
    username = args.user

    print(f"\n🔍 Fetching GitHub data for: {username} ...")
    data = get_summary_data(username)

    if not data:
        print(f"❌ Could not fetch data for '{username}'. Check the username and try again.")
        sys.exit(1)

    print(f"🤖 Analyzing profile with Gemini AI ...")
    insights = analyze_profile(data)

    print_report(data, insights)

    if args.save:
        save_report(data, insights)


if __name__ == "__main__":
    main()
