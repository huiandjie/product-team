from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

from .tools.file_tool import FileWriterTool
from .tools.jira_issue_creator_tool import JiraIssueCreatorTool
from .tools.jira_story_creator_tool import JiraStoryCreatorTool
from .tools.jira_epic_creator_tool import JiraEpicCreatorTool
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class ProjectTeam():
    """ProjectTeam crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools

    @agent
    def project_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['product_manager'], # type: ignore[index]
            tools=[JiraEpicCreatorTool()],
            verbose=True
        )

    @agent
    def business_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['business_analyst'], # type: ignore[index]
            tools=[JiraIssueCreatorTool()],
            verbose=True
        )

    @agent
    def product_owner(self) -> Agent:
        return Agent(
            config=self.agents_config['product_owner'], # type: ignore[index]
            tools=[JiraStoryCreatorTool()],
            verbose=True
        )

    @agent
    def solution_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['solution_architect'], # type: ignore[index]
            verbose=True
        )    

    @agent
    def backend_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['backend_engineer'], # type: ignore[index]
            tools=[FileWriterTool()],
            verbose=True
        )   

    @agent
    def frontend_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['frontend_engineer'],
            tools=[FileWriterTool()],
            verbose=True,
        )
    
    @agent
    def test_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['test_engineer'],
            tools=[FileWriterTool()],
            verbose=True,
          #  allow_code_execution=True,
          #  code_execution_mode="safe",  # Uses Docker for safety
           # max_execution_time=500, 
           # max_retry_limit=3 
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def planing_task(self) -> Task:
        return Task(
            config=self.tasks_config['planing_task'], # type: ignore[index]
            # agent assignment removed; handled in tasks.yaml

            
        )


    @task
    def application_task(self) -> Task:
        return Task(
            config=self.tasks_config['application_task'], # type: ignore[index]
            # agent assignment removed; handled in tasks.yaml
        )

    @task
    def feature_task(self) -> Task:
        return Task(
            config=self.tasks_config['feature_task'], # type: ignore[index]
            # agent assignment removed; handled in tasks.yaml
        )

    @task
    def architecture_task(self) -> Task:
        return Task(
            config=self.tasks_config['architecture_task'], # type: ignore[index]
            # agent assignment removed; handled in tasks.yaml
        )


    @task
    def code_task(self) -> Task:
        return Task(
            config=self.tasks_config['code_task'], # type: ignore[index]
            # agent assignment removed; handled in tasks.yaml
        )

    @task
    def frontend_task(self) -> Task:
        return Task(
            config=self.tasks_config['frontend_task'],
            # agent assignment removed; handled in tasks.yaml
        )

    @task
    def test_task(self) -> Task:
        return Task(
            config=self.tasks_config['test_task'],
            # agent assignment removed; handled in tasks.yaml
        )         


    @crew
    def crew(self) -> Crew:
        """Creates the ProjectTeam crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
    
# class AgileCrew():ec
#     """AgileCrew crew"""
#     def run(self, input):
                
#         result = ProjectTeam().crew().kickoff(inputs=input)
#         return str(result)

