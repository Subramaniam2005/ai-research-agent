def build_prompt(question, results):
    joined_results = "\n".join(results)
    return f"""
Answer the question using the information below.

Question:
{question}

Information:
{joined_results}

Give a short clear answer.
"""
