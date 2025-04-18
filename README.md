# 🧠 RepoAuditorCrew – Agentic GitHub Repo Auditor

## 🎯 Main Objective

The `RepoAuditorCrew` automates the end-to-end auditing of a public GitHub repository by executing a sequence of intelligent agent tasks. It is designed to:

1. **Clone** a repository from a provided `repo_url`
2. **Inspect** the repository structure (e.g., `README.md`, `requirements.txt`, `Dockerfile`, entry points like `app.py`)
3. **Run** the project by installing dependencies and executing its main script
4. **Review** the run output or error logs, then suggest fixes or confirm successful execution

## 🔍 Use Cases

- Automated open-source repo evaluations
- Technical due diligence for new projects
- Onboarding checks for team-contributed code
- Bootstrapping code understanding for LLM agents

## 🚀 Bonus Ideas for Extension

- Add license detection
- Integrate code quality or linting checks
- Check for known vulnerabilities
- Generate structured reports (Markdown or PDF)


------------------------------------------------------------

# NewProject Crew

Welcome to the NewProject Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/new_project/config/agents.yaml` to define your agents
- Modify `src/new_project/config/tasks.yaml` to define your tasks
- Modify `src/new_project/crew.py` to add your own logic, tools and specific args
- Modify `src/new_project/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the new_project Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The new_project Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the NewProject Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
