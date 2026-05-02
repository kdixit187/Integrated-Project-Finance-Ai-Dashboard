import streamlit as st
from crewai import Agent, Task, Crew
import os

# -------- ENV --------
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")
os.environ["OPENAI_BASE_URL"] = "https://api.groq.com/openai/v1"

# -------- AGENTS --------
def analyst():
    return Agent(
        role="Financial Analyst",
        goal="Analyze stock and give insights",
        backstory="Expert in stock market trends",
        llm="llama-3.1-8b-instant",
        verbose=False
    )

def reporter():
    return Agent(
        role="Report Generator",
        goal="Create clean financial report",
        backstory="Formats analysis into readable insights",
        llm="llama-3.1-8b-instant",
        verbose=False
    )

# -------- TASKS --------
def analyze_task(agent, stock):
    return Task(
        description=f"""
        Analyze stock {stock}.
        Give:
        - Overview
        - Financial Performance
        - Growth Drivers
        - Risks
        """,
        agent=agent,
        expected_output="Detailed analysis"
    )

def report_task(agent, stock):
    return Task(
        description=f"""
        Create a structured report for {stock}.
        Format clearly with headings.
        """,
        agent=agent,
        expected_output="Final report"
    )

# -------- CREW --------
def run_crew(stock):
    a = analyst()
    r = reporter()
    crew = Crew(
        agents=[a, r],
        tasks=[analyze_task(a, stock), report_task(r, stock)],
        verbose=False
    )
    return crew.kickoff()

# -------- PAGE CONFIG --------
st.set_page_config(page_title="FinAI Terminal", layout="wide", page_icon="▸")

# -------- CSS --------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@300;400;500;600&family=IBM+Plex+Sans:wght@300;400;600&display=swap');

/* ── Root reset ── */
html, body, [class*="css"] {
    font-family: 'IBM Plex Sans', sans-serif;
    background-color: #020A08 !important;
    color: #C8D8C8 !important;
}

.stApp {
    background-color: #020A08 !important;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 3rem 4rem 3rem !important; max-width: 1200px; }

/* ── Header bar ── */
.fin-header {
    display: flex;
    align-items: baseline;
    gap: 18px;
    border-bottom: 1px solid #1a3329;
    padding-bottom: 18px;
    margin-bottom: 36px;
}

.fin-wordmark {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #2EE88A;
}

.fin-submark {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.12em;
    color: #3A5C4A;
    text-transform: uppercase;
}

.fin-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #2EE88A;
    display: inline-block;
    margin-right: 8px;
    box-shadow: 0 0 8px #2EE88A88;
    animation: blink 2s ease-in-out infinite;
}

@keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.2; }
}

/* ── Hero title ── */
.fin-hero {
    margin-bottom: 40px;
}

.fin-title {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 46px;
    font-weight: 600;
    line-height: 1.1;
    color: #E8F4EC;
    letter-spacing: -0.02em;
    margin-bottom: 8px;
}

.fin-title span {
    color: #2EE88A;
}

.fin-desc {
    font-size: 14px;
    color: #3A5C4A;
    font-family: 'IBM Plex Mono', monospace;
    letter-spacing: 0.05em;
}

/* ── Input area ── */
.stTextInput > div > div {
    background: #040F0A !important;
    border: 1px solid #1a3329 !important;
    border-radius: 2px !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 22px !important;
    color: #2EE88A !important;
    letter-spacing: 0.08em !important;
    padding: 14px 18px !important;
    transition: border-color 0.2s;
}

.stTextInput > div > div:focus-within {
    border-color: #2EE88A !important;
    box-shadow: 0 0 0 1px #2EE88A20, 0 0 16px #2EE88A10 !important;
}

.stTextInput > div > div > input {
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 22px !important;
    color: #2EE88A !important;
    background: transparent !important;
    caret-color: #2EE88A;
}

.stTextInput > div > div > input::placeholder {
    color: #1F3D2E !important;
    font-size: 16px !important;
    letter-spacing: 0.04em;
}

.stTextInput label {
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 10px !important;
    letter-spacing: 0.18em !important;
    text-transform: uppercase !important;
    color: #3A5C4A !important;
    margin-bottom: 6px !important;
}

/* ── Button ── */
.stButton > button {
    background: #2EE88A !important;
    color: #020A08 !important;
    border: none !important;
    border-radius: 2px !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 11px !important;
    font-weight: 600 !important;
    letter-spacing: 0.2em !important;
    text-transform: uppercase !important;
    padding: 14px 32px !important;
    height: auto !important;
    width: 100% !important;
    transition: background 0.15s, box-shadow 0.15s !important;
    cursor: pointer !important;
}

.stButton > button:hover {
    background: #4BFFAA !important;
    box-shadow: 0 0 20px #2EE88A40 !important;
}

.stButton > button:active {
    background: #1ACC6E !important;
}

/* ── Spinner ── */
.stSpinner > div {
    border-top-color: #2EE88A !important;
}

/* ── Section label ── */
.section-label {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.24em;
    text-transform: uppercase;
    color: #2EE88A;
    border-left: 2px solid #2EE88A;
    padding-left: 10px;
    margin-bottom: 16px;
    margin-top: 32px;
}

/* ── Result panels ── */
.result-panel {
    background: #040F0A;
    border: 1px solid #1a3329;
    border-top: 2px solid #2EE88A;
    padding: 28px 32px;
    margin-bottom: 20px;
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 14.5px;
    line-height: 1.8;
    color: #A8C4B0;
}

/* ── Divider ── */
.stDivider {
    border-color: #1a3329 !important;
}
hr {
    border: none !important;
    border-top: 1px solid #1a3329 !important;
    margin: 32px 0 !important;
}

/* ── Markdown inside panels ── */
.result-panel h2, .result-panel h3 {
    font-family: 'IBM Plex Mono', monospace;
    color: #E8F4EC;
    font-size: 13px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-top: 24px;
    margin-bottom: 8px;
}

.result-panel p {
    margin-bottom: 12px;
}

.result-panel strong {
    color: #E8F4EC;
}

/* ── Status bar ── */
.status-bar {
    display: flex;
    gap: 32px;
    margin-top: 40px;
    padding-top: 16px;
    border-top: 1px solid #1a3329;
}

.status-item {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.1em;
    color: #3A5C4A;
}

.status-item span {
    color: #2EE88A;
    margin-right: 6px;
}
</style>
""", unsafe_allow_html=True)

# -------- HEADER --------
st.markdown("""
<div class="fin-header">
    <div class="fin-wordmark"><span class="fin-dot"></span>FINAI TERMINAL</div>
    <div class="fin-submark">Multi-Agent Research System v2.0</div>
</div>
""", unsafe_allow_html=True)

# -------- HERO --------
st.markdown("""
<div class="fin-hero">
    <div class="fin-title">AI-Powered<br><span>Stock Intelligence</span></div>
    <div class="fin-desc">// dual-agent analysis · groq llm inference · realtime synthesis</div>
</div>
""", unsafe_allow_html=True)

# -------- INPUT ROW --------
col1, col2 = st.columns([4, 1], gap="medium")

# -------- ENTER-TO-APPLY (press Enter in the text field to trigger run) --------
if "run_pressed" not in st.session_state:
    st.session_state["run_pressed"] = False

def _enter_submit():
    st.session_state["run_pressed"] = True

with col1:
    stock = st.text_input(
        "TICKER SYMBOL",
        placeholder="e.g.  AAPL  ·  NVDA  ·  TSLA",
        key="stock_input",
        on_change=_enter_submit
    )

with col2:
    st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)
    run = st.button("▸ RUN ANALYSIS")

    # treat Enter (session flag) the same as pressing the Run button
    triggered = run or st.session_state.get("run_pressed", False)

# -------- OUTPUT --------
if triggered and stock:
    stock_upper = stock.strip().upper()

    with st.spinner(f"Dispatching agents for {stock_upper}..."):
        result = run_crew(stock_upper)

    tasks = result.tasks_output
    analysis = tasks[0].raw if len(tasks) > 0 else "No analysis returned."
    report   = tasks[1].raw if len(tasks) > 1 else "No report returned."

    # Clean up markdown artifacts from LLM
    def clean(text):
        return text.replace("**", "").strip()

    st.markdown(f'<div class="section-label">01 — Analyst Output · {stock_upper}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="result-panel">', unsafe_allow_html=True)
    st.markdown(clean(analysis))
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="section-label">02 — Synthesized Report · {stock_upper}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="result-panel">', unsafe_allow_html=True)
    st.markdown(clean(report))
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="status-bar">
        <div class="status-item"><span>◈</span> TICKER: {stock_upper}</div>
        <div class="status-item"><span>◈</span> AGENTS: 2 COMPLETED</div>
        <div class="status-item"><span>◈</span> MODEL: llama-3.1-8b-instant</div>
        <div class="status-item"><span>◈</span> STATUS: SUCCESS</div>
    </div>
    """, unsafe_allow_html=True)

    # reset enter flag after handling
    st.session_state["run_pressed"] = False

elif triggered and not stock:
    st.warning("Enter a stock symbol to begin analysis.")
    st.session_state["run_pressed"] = False

# -------- FOOTER --------
else:
    st.markdown("""
    <div class="status-bar">
        <div class="status-item"><span>◈</span> AGENTS: STANDBY</div>
        <div class="status-item"><span>◈</span> BACKEND: GROQ / CREWAI</div>
        <div class="status-item"><span>◈</span> ENTER TICKER TO BEGIN</div>
    </div>
    """, unsafe_allow_html=True)