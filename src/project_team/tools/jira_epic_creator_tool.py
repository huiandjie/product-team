from jira import JIRA
from crewai.tools import BaseTool
from dotenv import load_dotenv
import os
from .jira_issue_creator_tool import JiraIssueCreatorTool

class JiraEpicCreatorTool(JiraIssueCreatorTool):
    name: str = "JiraEpicCreatorTool"
    description: str = (
        """
        This tool is able to create a Jira Epic using summary, description.
        """
    )

    def _run(self, summary: str, description: str):
        return super()._run(summary, description, "Epic")


if __name__ == "__main__":
    tool = JiraEpicCreatorTool()
    key = tool._run(
        "create an epic", "this is an epic description"
    )
    print(f"Key: {key}")
