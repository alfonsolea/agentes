import os
from dotenv import load_dotenv
from crewai.project import CrewBase, agent, crew, task
from crewai import Agent, Crew, Process, Task
from langchain_google_genai import ChatGoogleGenerativeAI
import langchain
import sys
print(sys.path)
print(langchain.__file__)
print("Importación exitosa")

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


@CrewBase
class BackendDevelopmentCrew:
    def __init__(self, workplan_content=None):
        self.agents_config = 'config/agents.yaml'
        self.tasks_config = 'config/tasks.yaml'
        self.workplan_content = workplan_content
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro-exp-0801",
            verbose=True,
            temperature=0.5,
            google_api_key=GEMINI_API_KEY
        )

    @agent
    def project_leader(self) -> Agent:
        return Agent(
            config=self.agents_config['project_leader'],
            verbose=True,
            llm=self.llm,
            memory=True
        )

    @agent
    def backend_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['backend_developer'],
            verbose=True,
            llm=self.llm,
            memory=True
        )

    @agent
    def backend_code_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['backend_code_reviewer'],
            verbose=True,
            llm=self.llm,
            memory=True
        )

    @agent
    def database_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['database_engineer'],
            verbose=True,
            llm=self.llm,
            memory=True
        )

    @agent
    def microservices_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['microservices_architect'],
            verbose=True,
            llm=self.llm,
            memory=True
        )

    @agent
    def microservice_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['microservice_developer'],
            verbose=True,
            llm=self.llm,
            memory=True
        )

    @task
    def analyze_workplan_task(self) -> Task:
        config = self.tasks_config['analyze_workplan_task']
        return Task(
            description=config['description'],
            expected_output=config['expected_output'],
            agent=self.project_leader(),
            context=[{"description": config['description'], "expected_output":
                      config['expected_output'], "workplan_content": self.workplan_content}]
        )

    @task
    def setup_project_task(self) -> Task:
        config = self.tasks_config['setup_project_task']
        return Task(
            description=config['description'],
            expected_output=config['expected_output'],
            agent=self.backend_developer(),
            context=[{"description": config['description'], "expected_output":
                      config['expected_output'], "workplan_content": self.workplan_content}]
        )

    @task
    def implement_crud_endpoints_task(self) -> Task:
        config = self.tasks_config['implement_crud_endpoints_task']
        return Task(
            description=config['description'],
            expected_output=config['expected_output'],
            agent=self.backend_developer(),
            context=[{"description": config['description'], "expected_output":
                      config['expected_output'], "workplan_content": self.workplan_content}]
        )

    @task
    def implement_custom_endpoints_task(self) -> Task:
        config = self.tasks_config['implement_custom_endpoints_task']
        return Task(
            description=config['description'],
            expected_output=config['expected_output'],
            agent=self.backend_developer(),
            context=[{"description": config['description'], "expected_output":
                      config['expected_output'], "workplan_content": self.workplan_content}]
        )

    @task
    def implement_auth_task(self) -> Task:
        config = self.tasks_config['implement_auth_task']
        return Task(
            description=config['description'],
            expected_output=config['expected_output'],
            agent=self.backend_developer(),
            context=[{"description": config['description'], "expected_output":
                      config['expected_output'], "workplan_content": self.workplan_content}]
        )

    @task
    def review_code_quality_task(self) -> Task:
        config = self.tasks_config['review_code_quality_task']
        return Task(
            description=config['description'],
            expected_output=config['expected_output'],
            agent=self.backend_code_reviewer(),
            context=[{"description": config['description'], "expected_output":
                      config['expected_output'], "workplan_content": self.workplan_content}]
        )

    @task
    def implement_code_improvements_task(self) -> Task:
        config = self.tasks_config['implement_code_improvements_task']
        return Task(
            description=config['description'],
            expected_output=config['expected_output'],
            agent=self.backend_code_reviewer(),
            context=[{"description": config['description'], "expected_output":
                      config['expected_output'], "workplan_content": self.workplan_content}]
        )

    @task
    def setup_database_task(self) -> Task:
        config = self.tasks_config['setup_database_task']
        return Task(
            description=config['description'],
            expected_output=config['expected_output'],
            agent=self.database_engineer(),
            context=[{"description": config['description'], "expected_output":
                      config['expected_output'], "workplan_content": self.workplan_content}]
        )

    @task
    def design_microservices_architecture_task(self) -> Task:
        config = self.tasks_config['design_microservices_architecture_task']
        return Task(
            description=config['description'],
            expected_output=config['expected_output'],
            agent=self.microservices_architect(),
            context=[{"description": config['description'], "expected_output":
                      config['expected_output'], "workplan_content": self.workplan_content}]
        )

    @task
    def implement_microservice_task(self) -> Task:
        config = self.tasks_config['implement_microservice_task']
        return Task(
            description=config['description'],
            expected_output=config['expected_output'],
            agent=self.microservice_developer(),
            context=[{"description": config['description'], "expected_output":
                      config['expected_output'], "workplan_content": self.workplan_content}]
        )

    @task
    def integrate_microservices_task(self) -> Task:
        config = self.tasks_config['integrate_microservices_task']
        return Task(
            description=config['description'],
            expected_output=config['expected_output'],
            agent=self.microservice_developer(),
            context=[{"description": config['description'], "expected_output":
                      config['expected_output'], "workplan_content": self.workplan_content}]
        )

    @task
    def setup_database_for_microservice_task(self) -> Task:
        config = self.tasks_config['setup_database_for_microservice_task']
        return Task(
            description=config['description'],
            expected_output=config['expected_output'],
            agent=self.microservice_developer(),
            context=[{"description": config['description'], "expected_output":
                      config['expected_output'], "workplan_content": self.workplan_content}]
        )

    @task
    def finalize_project_task(self) -> Task:
        config = self.tasks_config['finalize_project_task']
        return Task(
            description=config['description'],
            expected_output=config['expected_output'],
            agent=self.project_leader(),
            output_file='final_project.zip',
            context=[{"description": config['description'], "expected_output":
                      config['expected_output'], "workplan_content": self.workplan_content}]
        )

    @crew
    def crew(self) -> Crew:
        """Crea el Backend Development crew"""
        return Crew(
            agents=[
                self.backend_developer(),
                self.backend_code_reviewer(),
                self.database_engineer(),
                self.microservices_architect(),
                self.microservice_developer()
            ],  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.hierarchical,
            verbose=2,
            manager_agent=self.project_leader(),
            language='es'
        )

    def kickoff(self, inputs=None):
        if inputs is None:
            inputs = {'workplan_content': self.workplan_content}
        return self.crew().kickoff(inputs)
