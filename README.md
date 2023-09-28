# streamlit_stream
Bedrock streaming with OpenAI style

# Requirements:
    boto3
    streamlit

# Usage:
```python
from streamlit_stream import st_stream_bedrock

bedrock = boto3.client()
prompt = 'Lets see some streaming action'

# Titan parameters
model_params = {'inputText': prompt,
                'textGenerationConfig': {
                    'maxTokenCount': 0,
                    'stopSequences': [],
                    temperature': 0,
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

submit_button = st.button('Submit', type='primary)
box = st.empty()
    
    if submit_button:
        st_stream_bedrock(bedrock_client, model_params, box, modelId='amazon.titan-t1-large')```



