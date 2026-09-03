# AI Meets Agile: How CrewAI Transforms Project Management and Development.

![Project Team](assets/project-team.png)

Discover how CrewAI brings automation and intelligence to Agile project management and software development. This session demonstrates an end-to-end workflow where AI agents — acting as project manager, business analyst, product owner, architect, developers, and QA engineer — collaborate to plan, design, code, and test an application like an e-commerce site. Participants will learn how multi-agent systems can accelerate delivery, improve consistency, and free human teams to focus on innovation and strategic thinking.


## CrewAI
Python-based multi-agent orchestration framework/library, which is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

Major Components:
- **Agents**: Autonomous AI entities with specific roles, goals, and tools.
- **Tasks**: Defined objectives that agents work on collaboratively.
- **Crew**: The central orchestrator that manages the lifecycle of agents and tasks.
- **Tools**: External utilities and APIs that agents can leverage to enhance their capabilities.


## Getting Started
Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

next , install crewAI globally:

```bash
uv install crewai
```

create a new project:

```bash
crewai create crew {project_name}
```


Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/project_team/config/agents.yaml` to define your agents
- Modify `src/project_team/config/tasks.yaml` to define your tasks
- Modify `src/project_team/crew.py` to add your own logic, tools and specific args
- Modify `src/project_team/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the project_team Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The project_team Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the ProjectTeam Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
