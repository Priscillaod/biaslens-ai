import streamlit as st

from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a healthcare language bias reviewer."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.2,
    max_tokens=800
)
result = response.choices[0].message.content
git add .

st.set_page_config(page_title="BiasLens AI", layout="wide")

st.title(" BiasLens AI")
st.subheader("Scan clinical notes for biased or non-inclusive language using Azure OpenAI")

# Text input area
user_input = st.text_area("Paste your clinical note below:", height=200)

if st.button("Analyze for Bias"):
    if user_input.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        with st.spinner("Analyzing..."):
            prompt = f"""
You are an expert in inclusive healthcare documentation. Review the following clinical note and identify any potentially biased or non-inclusive language related to gender, race, age, or ability.

- Highlight biased phrases.
- Explain why each is problematic.
- Suggest an inclusive rewrite.

Text:
\"\"\"{user_input}\"\"\"
"""
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a healthcare language bias reviewer."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.2,
                    max_tokens=800
                )
                result = response['choices'][0]['message']['content']
                st.success("Analysis Complete ✅")
                st.markdown(result)
            except Exception as e:
                st.error(f"Error: {e}")
