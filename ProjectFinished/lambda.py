# ---- AWS Lambda (1st Lambda):     Image Serializer 
import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    key = event["s3_key"]
    bucket = event["s3_bucket"]
    
    s3.download_file(bucket, key, "/tmp/image.png")
    
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read()).decode("utf-8")
    event['image_data'] = image_data
    
    # return event
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    }

# ---- AWS Lambda (2nd Lambda):      Image prediction
import json
import base64
from sagemaker.predictor import Predictor
from sagemaker.serializers import IdentitySerializer

ENDPOINT = "scones-unlimited-endpoint"

def lambda_handler(event, context):
    image = base64.b64decode(event["image_data"])

    predictor = Predictor(endpoint_name=ENDPOINT)
    predictor.serializer = IdentitySerializer("image/png")

    inferences = predictor.predict(image)

    event["inferences"] = json.loads(inferences.decode("utf-8"))

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }



# ---- AWS Lambda (3rd Lambda):     Monitor Bad Predictions
import json

THRESHOLD = 0.93

def lambda_handler(event, context):
    print("lambda: ", event)

    # 1. Check key exists
    if "inferences" not in event:
        raise ValueError("Missing 'inferences' key in input event")

    inferences = event["inferences"]

    # 2. Validate it's a list with exactly 2 items
    if not isinstance(inferences, list):
        raise TypeError("'inferences' must be a list")
    if len(inferences) != 2:
        raise ValueError("'inferences' must contain exactly 2 elements")

    # 3. Ensure all elements are float (or convertible to float)
    try:
        inferences = [float(x) for x in inferences]
    except Exception:
        raise ValueError("All values in 'inferences' must be convertible to float")

    # 4. Business logic: evaluate only the first probability:   Bicycle in position ZERO
    if inferences[0] < THRESHOLD:
        raise Exception("THRESHOLD_CONFIDENCE_NOT_MET")

    # 5. Return event if all checks pass
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }

    
