from crewai import Task

def analyze(agent, stock):
    return Task(
        description=f"Analyze stock {stock}",
        agent=agent,
        expected_output="Analysis"
    )

def report(agent, stock):
    return Task(
        description=f"Generate report for {stock}",
        agent=agent,
        expected_output="Final report"
    )