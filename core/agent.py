from mistralai import Mistral

import os


def get_mistral_client():
    return Mistral(api_key=os.getenv("MISTRAL_API_KEY"))


def create_omni_agent(client):
    agent = client.beta.agents.create(
        model = "mistral-medium-2508",
        name = "Omni-analyst",
        instructions=(
            "You are a Senior Data Analyst."
            "Step 1: Use web_seach to find the latest data resquested."
            "step 2: Use code_interpreter to clean the data and create a visualisation."
            "step 3: Output a professional Markdown report with the findings."
        ),
        tools=[
            {"type": "web_search"},
            {"type": "code_interpreter"}
        ]

    )
    return agent.id



