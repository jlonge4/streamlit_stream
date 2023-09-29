import openai
import time

openai.api_key = ''

def stream(model, prompt, box):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            # {'role': 'user', 'content': "prompt"}
            prompt
        ],
        temperature=0,
        stream=True  
    )
    if response:
        s = ''
        for chunk in response:
            if chunk['choices'][0]['finish_reason'] == "stop":
                break
            for c in chunk['choices'][0]['delta']['content']:
                s += c
                time.sleep(.002)
                box.write(s)
