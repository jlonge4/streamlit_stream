# streamlit_stream
Bedrock streaming with OpenAI style

# Usage:
from streamlit_stream import st_stream_bedrock

model_params = {}

submit_button = st.button('Submit', type='primary)

box = st.empty()

if submit_button:
    st_stream_bedrock(bedrock_client, model_params, box)
