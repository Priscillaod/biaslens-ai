import streamlit as st
from dotenv import load_dotenv
import os
from openai import AzureOpenAI

# Load environment variables from .env file in the parent directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# Get API key from .env
api_key = os.getenv("AZURE_OPENAI_KEY")

# Ensure key is loaded
if not api_key:
    st.error("❌ API key not found. Please check your .env file and key name.")
    st.stop()

# Set up Azure OpenAI client
client = AzureOpenAI(
    api_key=api_key,
    api_version="2024-12-01-preview",
    azure_endpoint="https://ai-craftdashlimited772104474304.cognitiveservices.azure.com/"
)

# Streamlit UI
st.set_page_config(page_title="BiasLens AI", layout="wide")
st.title("🧠 BiasLens AI")
st.subheader("Scan clinical notes for biased or non-inclusive language using Azure OpenAI")

user_input = st.text_area("Paste your clinical note below:", height=200)

if st.button("Analyze for Bias"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text to analyze.")
    else:
        with st.spinner("Analyzing..."):
            prompt = f"""
You are an expert in inclusive healthcare documentation. Review the following clinical note and identify any potentially biased or non-inclusive language related to gender, race, or age.

- Highlight biased phrases.
- Explain why each is problematic.
- Suggest an inclusive rewrite.

Text:
\"\"\"{user_input}\"\"\"
"""
            try:
                response = client.chat.completions.create(
                    model="gpt-4o",  # Your Azure deployment name
                    messages=[
                        {"role": "system", "content": "You are a healthcare language bias reviewer."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.2,
                    max_tokens=800
                )

                result = response.choices[0].message.content
                st.success("✅ Analysis Complete")
                st.markdown(result)

            except Exception as e:
                st.error(f"❌ Error: {e}")
