import json
import boto3
import time

def st_stream(client: boto3.Session.client, model_kwargs: dict, box, modelid):
  def stream_ titan(client, model _kwargs):
    cont = True
    while cont:
      response_stream - client.invoke _model_with_response_stream(
      body-json.dumps (model _kwargs), modelid-"amazon.titan-tg1-large' accept-'application/json', contentType-'application/json'
              T
        )
      status_code - response_stream[ ResponseMetadata '1[ 'HTTPStatusCode*] 
      if status_code != 200:
      raise ValueError
f*Error invoking Bedrock API: (status _code}" for response in response_stream[ 'body'!:
json_response - json. loads(response[* chunk'J[ 'bytes ' 1)
yield json_response[ 'outputText *]
if json _response[' completionReason *] =- 'FINISH':
cont = False
break
def stream_claude(client, model_kwargs) :
response_stream - client. invoke_model with_response_stream
body-json. dumps (model_kwargs), modelId-"anthropic. claude-v2" accept-'application/json' contentType-'application/json'
if response_stream:
status_code - response_stream ResponseMetadata'JI'HTTPStatusCode*]
if status_code !- 200:
raise ValueError
f*Error invoking Bedrock API: (status_code)"
)
for response in response_stream[ 'body*]:
json_response - json.loads(response [ 'chunk I['bytes '1)
yield json_response[ 'completion']
if modelid == amazon.titan-tg1-large
§ = ""
for p in stream_titan(client, model _kwargs):
for c in r:
§ += C
time. sleep(.002)
box .write(s)
else:
S = "*
for r in stream_claude (client, model _kwargs):
for c in p:
§ += с
time. sleep (.002)
box.write(s)