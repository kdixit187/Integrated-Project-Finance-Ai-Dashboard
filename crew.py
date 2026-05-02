from crewai import Crew
from agents import analyst, reporter
from tasks import analyze, report

def run_crew(stock):
    a = analyst()
    r = reporter()

    crew = Crew(
        agents=[a, r],
        tasks=[
            analyze(a, stock),
            report(r, stock)
        ],
        verbose=False
    )

    return crew.kickoff()
