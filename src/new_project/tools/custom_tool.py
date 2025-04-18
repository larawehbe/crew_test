from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."


from pydantic import BaseModel, Field
from typing import Type

class CloneRepoInput(BaseModel):
    repo_url: str = Field(..., description="The public GitHub URL to clone.")

class CloneRepoTool(BaseTool):
    name: str = "Clone GitHub Repository"
    description: str = "Clones a public GitHub repository into a local folder called 'cloned_repo'."
    args_schema: Type[BaseModel] = CloneRepoInput

    def _run(self, repo_url: str) -> str:
        print("🔍 Received repo_url:", repo_url)
        import subprocess, os, shutil

        if os.path.exists("cloned_repo"):
            shutil.rmtree("cloned_repo")

        try:
            print(f"repo: {repo_url}")
            subprocess.run(["git", "clone", repo_url, "cloned_repo"], check=True)
            return "✅ Repository cloned successfully."
        except subprocess.CalledProcessError as e:
            return f"❌ Error while cloning: {e}"
