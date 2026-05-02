from crewai import Agent

def analyst():
    return Agent(
        role="Financial Analyst",
        goal="Analyze stock",
        backstory="Expert in stock trends",
        llm="llama-3.1-8b-instant",
        verbose=False
    )

def reporter():
    return Agent(
        role="Report Generator",
        goal="Summarize analysis",
        backstory="Creates reports",
        llm="llama-3.1-8b-instant",
        verbose=False
    )