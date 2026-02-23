import os
import base64

from dotenv import load_dotenv
from core.agent import get_mistral_client, create_omni_agent


load_dotenv()
def main():
    client = get_mistral_client()

    agent_id = create_omni_agent(client)

    user_query = "What is the market share of EV companies in Europe in 2024? Create a bar chart."

    print("Omni-analyst is thinking ...")

    response = client.beta.conversations.start(
        agent_id= agent_id,
        inputs=[{"role": "user", "content": f"f{user_query}"}]
    )

    print("\n--- FINAL REPORT ---")
    print(response.choices[0].message.content)
    if hasattr(response, 'tool_calls'):
        # In a real app, you would iterate through tool_calls to find
        # code_interpreter outputs and save them as PNGs.
        print("\n[System]: Chart data detected in tool calls.")

if __name__ == "__main__":
    main()