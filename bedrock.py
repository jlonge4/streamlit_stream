import json
import boto3
import time

def st_stream(client: boto3.Session.client, model_kwargs: dict, box, modelid):
  
  def stream_titan(client, model _kwargs):
      response_stream - client.invoke_model_with_response_stream(
        body = json.dumps(model_kwargs), 
        modelid='amazon.titan-tg1-large', 
        accept='application/json', 
        contentType='application/json'
      )
    if response_stream:
      status_code = response_stream['ResponseMetadata']['HTTPStatusCode'] 
    if status_code != 200:
      raise ValueError(f"Error invoking Bedrock API: {status_code}" 
    for response in response_stream['body']:
      json_response = json.loads(response['chunk']['bytes'])
      yield json_response['outputText']

                         
def stream_claude(client, model_kwargs) :
  response_stream = client.invoke_model with_response_stream(
    body=json.dumps(model_kwargs), 
    modelId="anthropic.claude-v2", 
    accept='application/json', 
    contentType='application/json'
  )
  if response_stream:
      status_code = response_stream ['ResponseMetadata']['HTTPStatusCode']
  if status_code != 200:
    raise ValueError(f"Error invoking Bedrock API: {status_code}")
  for response in response_stream['body']:
    json_response = json.loads(response['chunk']['bytes'])
    yield json_response['completion']
  
if modelid == 'amazon.titan-tg1-large':
  s = ""
  for r in stream_titan(client, model _kwargs):
    for c in r:
      s += c
      time.sleep(.002)
      box.write(s)

else:
  s = ""
  for r in stream_claude (client, model_kwargs):
    for c in r:
      s += с
      time.sleep(.002)
      box.write(s)
