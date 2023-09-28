import json
import boto3
import time

def st_stream_bedrock(client: boto3.Session.client, model_kwargs: dict, box):


  def get_chunks(client, model_kwargs):
    cont = True
    while cont:
      response_stream = client.invoke_model_with_response_stream(
        body=json.dumps(model_kwargs),
        model_Id='amazon.titan-tg1-large',
        accept='application/json',
        contentType='application/json')
      status_code = response_stream['ResponseMetadata']['HTTPStatusCode']
      if status_code != 200:
        raise ValueError(
          "Error during Bedrock invocation: {0}".format(status_code)
        )
      for response in response_stream['body']:
        json_response = json.loads(response['chunk']['bytes'])
        yield json_response['outputText']

        if json_response['completionReason'] == 'FINISH':
          cont = False
          break

  s = ''
  for r in get_chunks(client, model_kwargs):
    for char in r:
      s += char
      time.sleep(0.002)
      box.write(s)
