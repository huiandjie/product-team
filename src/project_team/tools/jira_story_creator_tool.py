from jira import JIRA
from crewai.tools import BaseTool
from dotenv import load_dotenv
import os
from .jira_issue_creator_tool import JiraIssueCreatorTool

class JiraStoryCreatorTool(JiraIssueCreatorTool):
    name: str = "JiraStoryCreatorTool"
    description: str = (
        """
        This tool is able to create a Jira Story using summary, description, type, parent key.
        """
    )

    def _run(self, summary: str, description: str, epic_key: str = "", feature_key: str = ""):
        load_dotenv()
        story_key = super()._run(summary, description, "Story", epic_key)

        if not story_key.startswith("MOCK-") and feature_key and feature_key not in ("None", "null", ""):
            try:
                jira_url = os.environ.get("JIRA_URL")
                username = os.environ.get("JIRA_USERNAME")
                api_token = os.environ.get("JIRA_API_TOKEN")
                if all([jira_url, username, api_token]):
                    jira = JIRA(options={"server": jira_url}, basic_auth=(username, api_token))
                    jira.create_issue_link("Relates", inwardIssue=story_key, outwardIssue=feature_key)
                    print(f"Story {story_key} linked to feature {feature_key} successfully.")
            except Exception as e:
                print(f"Could not link story to feature: {e}")

        return story_key


if __name__ == "__main__":
    tool = JiraStoryCreatorTool()
    key = tool._run(
        "create a button unit test", "create a material button unit test story", "SCRUM-58", "SCRUM-59"
    )
    print(f"Key: {key}")
