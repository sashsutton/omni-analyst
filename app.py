import os
from dotenv import load_dotenv
from mistralai import Mistral

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")

client = Mistral(api_key)



def test_connection():
    try:
        print("Sending request to Mistral ...")
        agent = client.beta.agents.create(
            model="mistral-medium-2505",
            name="Websearch Agent",
            instructions="You have the ability to perform web searches with `web_search` to find up-to-date information.",
            tools=[{"type": "web_search"}],
        )

        response = client.beta.conversations.start(
            agent_id=agent.id,
            inputs="Who is Albert Einstein?",
        )
        print(response)

    except Exception as e:
        print(f"\nOops, something went wrong: {e}")


if __name__ == "__main__":
    test_connection()
