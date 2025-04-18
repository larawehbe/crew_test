from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import subprocess
import os
import shutil

from new_project.tools.custom_tool import CloneRepoTool
from new_project.tools.inspect_tool import InspectRepoTool



@CrewBase
class RepoAuditorCrew():
    """Repo Auditor Crew to clone, inspect, run, and review a public GitHub repo"""

   
    @agent
    def cloner(self) -> Agent:
        return Agent(
            config=self.agents_config['cloner'],
            verbose=True,
            tools=[CloneRepoTool()],
        )

    @agent
    def inspector(self) -> Agent:
        return Agent(
            config=self.agents_config['inspector'],
            verbose=True,
            tools=[InspectRepoTool()],
        )

    @agent
    def runner(self) -> Agent:
        return Agent(
            config=self.agents_config['runner'],
            verbose=True
        )

    @agent
    def reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['reviewer'],
            verbose=True
        )

    
    @task
    def clone_repo(self) -> Task:
        return Task(
            description="""Use the cloning tool to clone the repository located at {repo_url}.  
            into a folder named 'cloned_repo'.""",
            expected_output="A confirmation message like 'Repository cloned successfully' or an error if it failed.",
            agent=self.cloner()
        )



    @task
    def inspect_repo(self) -> Task:
        return Task(
            description="Inspect the cloned repository and list all key files including README.md, requirements.txt, setup.py, Dockerfile, and any likely entry points such as app.py or main.py.",
            expected_output="A summary of the repository structure including detected setup files and possible entry points.",
            agent=self.inspector()
        )

    @task
    def run_repo(self) -> Task:

        return Task(
            description="Try to install dependencies (from requirements.txt if available) and run the project using the identified main script. Capture and return stdout and stderr output from the process.",
            expected_output="Full output from running the project, including success logs or any errors encountered.",
            agent=self.runner()
        )

    @task
    def review_errors(self) -> Task:
        return Task(
            description="Analyze the run output or error logs. Identify what went wrong (if anything), and suggest possible fixes or improvements to make the project runnable.",
            expected_output="A bullet-pointed summary of errors with suggestions or fixes to try. If no errors occurred, confirm successful execution.",
            agent=self.reviewer()
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Repo Auditor Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
