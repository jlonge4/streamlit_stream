import json
import boto3
import time


def stream(client: boto3.Session.client, model_kwargs: dict, box, modelid):
    # Function to stream Titan model response
    def stream_titan(client, model_kwargs):
        response_stream = client.invoke_model_with_response_stream(
            body=json.dumps(model_kwargs),
            modelId='amazon.titan-tg1-large',
            accept='application/json',
            contentType='application/json'
        )
        if response_stream:
            status_code = response_stream['ResponseMetadata']['HTTPStatusCode']
            if status_code != 200:
                raise ValueError(f"Error invoking Bedrock API: {status_code}")
            for response in response_stream['body']:
                json_response = json.loads(response['chunk']['bytes'])
                yield json_response['outputText']

    # Function to stream Claude model response
    def stream_claude(client, model_kwargs):
        response_stream = client.invoke_model_with_response_stream(
            body=json.dumps(model_kwargs),
            modelId="anthropic.claude-v2",
            accept='application/json',
            contentType='application/json'
        )
        if response_stream:
            status_code = response_stream['ResponseMetadata']['HTTPStatusCode']
            if status_code != 200:
                raise ValueError(f"Error invoking Bedrock API: {status_code}")
            for response in response_stream['body']:
                json_response = json.loads(response['chunk']['bytes'])
                yield json_response['completion']

    match modelid:
        case 'amazon.titan-tg1-large':
            s = ""
            for r in stream_titan(client, model_kwargs):
                for c in r:
                    s += c
                    time.sleep(.002)
                    box.write(s)
                    
        case "anthropic.claude-v2":
            s = ""
            for r in stream_claude(client, model_kwargs):
                for c in r:
                    s += c
                    time.sleep(.002)
                    box.write(s)
