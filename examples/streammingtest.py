import os
import openai
# optional; defaults to `os.environ['OPENAI_API_KEY']`

# all client options can be configured just like the `OpenAI` instantiation counterpart
openai.base_url = "http://0.0.0.0:8007/v1/"
openai.default_headers = {"x-foo": "true"}

completion = openai.chat.completions.create(
    model="Intel/neural-chat-7b-v3-3",
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion.choices[0].message.content)
