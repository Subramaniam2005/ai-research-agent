import sys
from search import web_search
from llm import call_llm
from prompts import build_prompt

if len(sys.argv) < 2:
    print("Usage: python agent.py \"your question\"")
    exit()

question = sys.argv[1]

print("Searching...")
results = web_search(question)

print("Thinking...")
prompt = build_prompt(question, results)
answer = call_llm(prompt)

print("\nFINAL ANSWER:\n")
print(answer)
