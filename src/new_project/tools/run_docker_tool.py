import os
import subprocess
from crewai.tools import BaseTool

class RunDockerTool(BaseTool):
    name: str = "RunDockerTool"
    description: str = "Builds and runs the Dockerfile found in the cloned_repo directory."

    def _run(self, **kwargs) -> str:
        print(f'running doker now!')
        repo_path = "cloned_repo"
        dockerfile_path = os.path.join(repo_path, "Dockerfile")

        if not os.path.isfile(dockerfile_path):
            return "❌ Dockerfile not found. Cannot run the project."

        try:
            # Build Docker image
            build_cmd = f"docker build -t audited_project {repo_path}"
            build_proc = subprocess.run(build_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            # Run Docker container
            run_cmd = "docker run --rm audited_project"
            run_proc = subprocess.run(run_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            return f"""✅ Dockerfile found.

                ### 🔨 Build Output:
                {build_proc.stdout}\n{build_proc.stderr}

                ### 🚀 Run Output:
                {run_proc.stdout}\n{run_proc.stderr}
            """

        except Exception as e:
            return f"❌ Error while running Docker: {str(e)}"

