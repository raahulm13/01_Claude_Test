import anthropic
import os

# My first agent

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "What are the top 3 risks in commercial real estate lending?"}
    ]
)

print(message.content[0].text)