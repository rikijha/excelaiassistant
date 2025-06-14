from openai import OpenAI
from pyxll import xl_func

client = OpenAI(api_key="Your_Key")

@xl_func()
def askAi(prompt:str, input:str) -> str:
    resp = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are excel data assitant provide data based with up to date knowledge"},
            {"role": "user", "content": f"${prompt} ${input}"}
        ],
        temperature=0.2,
        max_tokens=100
    )
    return resp.choices[0].message.content.strip()
