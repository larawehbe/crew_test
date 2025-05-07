#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

# from new_project.crew import NewProject
from new_project.crew import RepoAuditorCrew
from new_project.helpers import generate_report
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew with dynamic repo URL input.
    """
    # inputs = {
    #     "repo_url": "https://github.com/larawehbe/faulty-python-app"
    # }
    inputs = {
        "repo_url": "https://github.com/Nadine-kassir/collaborative-recommendation"
    }

    try:
        results = RepoAuditorCrew().crew().kickoff(inputs=inputs)
        task_outputs = results.tasks_output
        generate_report(inputs['repo_url'],task_outputs)
        print("✅ Report generated: repo_audit_report.md")
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")



# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {
#         "topic": "AI LLMs"
#     }
#     try:
#         RepoAuditorCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")

# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         RepoAuditorCrew().crew().replay(task_id=sys.argv[1])

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")

# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         "topic": "AI LLMs",
#         "current_year": str(datetime.now().year)
#     }
#     try:
#         RepoAuditorCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while testing the crew: {e}")
