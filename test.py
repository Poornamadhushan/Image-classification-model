import requests
import os


prediction_key = "prediction_key_here"
endpoint = "endpoint_here"  # e.g., "https://<your-custom-vision-resource-name>.cognitiveservices.azure.com/"
project_id = "project_id_here"  # Your Custom Vision project ID
published_name = " published_name_here"  # Name of the published iteration

image_path = r"Test image path here"

prediction_url = f"{endpoint}/customvision/v3.0/Prediction/{project_id}/classify/iterations/{published_name}/image"

headers = {
    "Prediction-Key": prediction_key,
    "Content-Type": "application/octet-stream"
}


if not os.path.exists(image_path):
    print(f"❌ Image not found: {image_path}")
    exit()

# Send image for prediction
with open(image_path, "rb") as image_file:
    response = requests.post(prediction_url, headers=headers, data=image_file.read())

# Print prediction result
if response.status_code == 200:
    predictions = response.json()["predictions"]
    print(f"\n✅ Predictions for {os.path.basename(image_path)}:")
    for result in predictions:
        print(f"🔹 {result['tagName']}: {result['probability']:.2%}")
else:
    print(f"❌ Prediction failed: {response.status_code}")
    print(response.text)
