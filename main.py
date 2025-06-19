import os
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from config import ENDPOINT, PREDICTION_KEY, PROJECT_ID, PUBLISHED_NAME
import glob

credentials = ApiKeyCredentials(in_headers={"Prediction-key": PREDICTION_KEY})
predictor = CustomVisionPredictionClient(ENDPOINT, credentials)

image_folder = "test-images"
for image_path in glob.glob(f"{image_folder}/*.jpg"):
    with open(image_path, "rb") as image_data:
        results = predictor.classify_image(PROJECT_ID, PUBLISHED_NAME, image_data.read())
    print(f"Results for {os.path.basename(image_path)}:")
    for prediction in results.predictions:
        print(f"{prediction.tag_name}: {prediction.probability:.2%}")
    print("---")
