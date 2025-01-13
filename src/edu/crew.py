from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Debug: Print API key (first few characters)
api_key = os.getenv('SERPER_API_KEY')
if api_key:
    print(f"API Key loaded (first 10 chars): {api_key[:10]}...")
else:
    print("Warning: SERPER_API_KEY not found in environment variables")
    raise ValueError("SERPER_API_KEY not found in environment variables")

@CrewBase
class MoojoLeadGen:
    """Moojo Lead Generation crew for finding companies needing privacy-preserving identity solutions"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self):
        super().__init__()
        self.search_tool = SerperDevTool(
            api_key=api_key,
            num_results=10
        )

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[self.search_tool],
            verbose=True,
            allow_delegation=False
        )

    @agent
    def privacy_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['privacy_analyst'],
            tools=[self.search_tool],
            verbose=True,
            allow_delegation=False
        )

    @agent
    def ai_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['ai_analyst'],
            tools=[self.search_tool],
            verbose=True,
            allow_delegation=False
        )

    @agent
    def outreach_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['outreach_strategist'],
            tools=[],
            verbose=True,
            allow_delegation=False
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task']
        )

    @task
    def privacy_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['privacy_analysis_task']
        )

    @task
    def ai_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['ai_analysis_task']
        )

    @task
    def final_report_task(self) -> Task:
        return Task(
            config=self.tasks_config['final_report_task']
        )

    @task
    def outreach_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['outreach_strategy_task']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Moojo Lead Generation crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )

# Create the crew instance
crew = MoojoLeadGen().crew()
