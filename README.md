# streamlit_stream
LLM streaming within streamlit, chatGPT style.

https://github.com/jlonge4/streamlit_stream/assets/91354480/fc5c2f20-5490-4bfe-84df-a880c96d2237

# Requirements:
    boto3
    streamlit
    openai

# Usage:
```python
### OPENAI ###

import streamlit as st
from streamlit_stream import openai_st


st.set_page_config(page_title='St_Stream', page_icon=':robot_face: ')
st.title('LLM Streaming with streamlit!')
input = st.text_area('Prompt...')
submit_button = st.button('Submit', type='primary')
box = st.empty()

prompt = {'role': 'user', 'content': input}

if submit_button and input:
    openai_st.stream(model='gpt-3.5-turbo', prompt=prompt, box=box)



### BEDROCK ### 
from streamlit_stream import bedrock_st

bedrock = boto3.client()
prompt = 'Lets see some streaming action'
modelId = 'amazon.titan-t1-large'
# Titan parameters
model_params = {'inputText': prompt,
                'textGenerationConfig': {
                    'maxTokenCount': 0,
                    'stopSequences': [],
                    'temperature': 0,
                    'topP':0,
                    },
                }

# Claude parameters
model_params = {'prompt': prompt,
                'max_tokens_to_sample':0,
                'temperature':0,
                'top_k':0,
                'stop_sequences':[],
                }

submit_button = st.button('Submit', type='primary')
box = st.empty()
    
    if submit_button:
        bedrock_st.stream(bedrock, model_params, box, modelId=modelId)



