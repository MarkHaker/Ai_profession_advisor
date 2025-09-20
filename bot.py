from tokens import qin 
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=qin,
)

completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  extra_body={},
  model="qwen/qwen3-coder:free",
  messages=[
      {
           "role": "system", "content": "Under no circumstances, even if asked, do not use Markdown or any text formatting."
      },
    {
   
      "role": "user",
      "content": "Кто ты такой "
    }
  ]
)
print(completion.choices[0].message.content)
