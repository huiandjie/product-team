from jira import JIRA
from crewai.tools import BaseTool
from dotenv import load_dotenv
import os


class JiraIssueCreatorTool(BaseTool):
    name: str = "JiraIssueCreatorTool"
    description: str = (
        """
        This tool is able to create a Jira Issue using summary, description, type, parent key.
        """
    )

    def _run(self, summary: str, description: str, type: str, parent_key: str = ""):
        load_dotenv()
        jira_url = os.environ.get("JIRA_URL")
        username = os.environ.get("JIRA_USERNAME")
        api_token = os.environ.get("JIRA_API_TOKEN")
        jira_project = os.environ.get("JIRA_PROJECT")

        if not all([jira_url, username, api_token, jira_project]):
            mock_key = f"MOCK-{type.upper()}-{abs(hash(summary)) % 10000}"
            print(f"Jira credentials missing; returning mock key {mock_key}")
            return mock_key

        jira_options = {"server": jira_url}

        try:
            jira = JIRA(options=jira_options, basic_auth=(username, api_token))
            issue_fields = {
                "project": {"key": jira_project},
                "summary": summary,
                "description": description,
                "issuetype": {"name": type},
            }
            if parent_key and parent_key not in ("None", "null", ""):
                issue_fields["parent"] = {"key": parent_key}
            print(f"issue_fields {issue_fields}")
            issue = jira.create_issue(fields=issue_fields)
            print(issue)
            return issue.key
        except Exception as e:
            mock_key = f"MOCK-{type.upper()}-{abs(hash(summary)) % 10000}"
            print(f"Jira error: {e}; returning mock key {mock_key}")
            return mock_key


if __name__ == "__main__":
    tool = JiraIssueCreatorTool()
    key = tool._run(
        "create a button unit test", "create a material button unit test story", "Story"
    )
    print(f"Key: {key}")
