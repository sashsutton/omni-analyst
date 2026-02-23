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

    full_report = ""

    for output in response.outputs:
        if hasattr(output, 'content'):
            for chunk in output.content:

                if chunk.type == 'text':
                    full_report += chunk.text

                if chunk.type == 'tool_file':
                    print(f"\n Found chart: {chunk.file_name} (ID: {chunk.file_id})")

                    file_response = client.files.download(file_id=chunk.file_id)

                    file_response.read()

                    save_path = os.path.join("exports/charts", chunk.file_name)

                    with open(save_path, "wb") as f:
                        f.write(file_response.content)

                    print(f" Chart successfully saved to {save_path}")

    print("\n--- FINAL REPORT ---")
    print(full_report)



if __name__ == "__main__":
    main()