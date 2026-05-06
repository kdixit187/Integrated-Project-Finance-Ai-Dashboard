python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY="your_groq_api_key"
streamlit run app.py
