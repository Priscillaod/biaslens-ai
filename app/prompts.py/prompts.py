def build_prompt(user_input):
    return f"""You are an expert in inclusive healthcare documentation. 
Review the following clinical note and identify any potentially biased or non-inclusive language. 

- Highlight biased phrases.
- Explain why each is problematic.
- Suggest an inclusive rewrite.

Text: "{user_input}"
"""