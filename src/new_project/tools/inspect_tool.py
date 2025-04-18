from crewai.tools import BaseTool
import os

class InspectRepoTool(BaseTool):
    name: str = "InspectRepoTool"
    description: str = "Lists key files in the cloned_repo directory such as README.md, requirements.txt, setup.py, Dockerfile, and likely entry points like main.py or app.py."

    def _run(self, **kwargs) -> str:
        repo_path = "cloned_repo"
        print("🔧 InspectRepoTool activated")
        if not os.path.exists(repo_path):
            return f"❌ Directory '{repo_path}' does not exist."

        output = ["📁 Repository Structure:\n"]
        for root, dirs, files in os.walk(repo_path):
            for file in files:
                rel_path = os.path.relpath(os.path.join(root, file), repo_path)
                output.append(f"- {rel_path}")
        
        return "\n".join(output)

