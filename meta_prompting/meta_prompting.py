#!/usr/bin/env python3
import os
from openai import OpenAI
import openai

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("No OPENAI_API_KEY found. Please set the environment variable.")
client = OpenAI(api_key=api_key)

GPT_MODEL = 'gpt-4o-mini'
PLANNING_MODEL = 'o1-preview'

def generate_routine(policy, o1_prompt):
    messages = [
        {
            'role': 'user',
            'content': f'{o1_prompt}\n POLICY:\n{policy}'
        }
    ]
    print(messages)

    response = client.chat.completions.create(
        model=PLANNING_MODEL,
        messages=messages
    )
    return response.choices[0].message.content 

def evaluate(test_cases):
    return 'score'

def optimize_routine():
    return

def main():
    with open('planning_prompt.md', 'r' ) as file:
        planning_prompt = file.read()
    
    with open('policy.md') as file:
        policy = file.read()

    print(generate_routine(policy, planning_prompt))



if __name__ == "__main__":
    main()
