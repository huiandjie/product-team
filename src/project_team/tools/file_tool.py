from crewai.tools import BaseTool
from pathlib import Path


class FileWriterTool(BaseTool):
    name: str = "FileWriterTool"
    description: str = (
        """
        This tool writes content to a file using a root path and a relative path.
        It automatically creates any missing directories.
        """
    )

    def _run(self, root_path: str, path: str, content: str) -> str:
        try:
            # Build full file path
            full_path = Path(root_path) / path

            # Create parent directories if they do not exist
            full_path.parent.mkdir(parents=True, exist_ok=True)

            # Write content to file
            full_path.write_text(content, encoding="utf-8")

            return f"File successfully written to {full_path}"

        except Exception as e:
            return f"Error writing file: {str(e)}"


if __name__ == "__main__":
    tool = FileWriterTool()
    result = tool._run(
        root_path="/tmp/my_project",
        path="data/output/result.txt",
        content="Hello from CrewAI tool!"
    )
    print(result)
