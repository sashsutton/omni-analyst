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
        inputs=[{"role": "user", "content": user_query}]
    )



    print("\n Final report: ")
    print(response)




if __name__ == "__main__":
    main()