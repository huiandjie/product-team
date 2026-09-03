from jira import JIRA
import sys
import os
from crewai.tools import BaseTool
from dotenv import load_dotenv

class JiraLinkStoryToFeatureTool(BaseTool):
    name: str = "JiraLinkStoryToFeatureTool"
    description: str = (
        """
        This tool is able to link a story to feature.
        """
    )

    def _run(self, story_key: str, feature_key: str = None):
        load_dotenv(override=True)
        jira_url = os.environ["JIRA_URL"]
        username = os.environ["JIRA_USERNAME"]
        api_token = os.environ["JIRA_API_TOKEN"]
        jira_project = os.environ["JIRA_PROJECT"]
        print(f"jira url is {jira_url}")
        jira_options = {"server": jira_url}
        try:
            # Connect to Jira
            jira = JIRA(options=jira_options, basic_auth=(username, api_token))


            jira.create_issue_link("Relates", inwardIssue=story_key, outwardIssue=feature_key)
            print(f"Story {story_key} linked to feature {feature_key} successfully.")

        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)

# Main function
if __name__ == "__main__":
   tool = JiraLinkStoryToFeatureTool()
   tool._run("SCRUM-46", "SCRUM-45")