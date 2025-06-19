# 🧠 Azure Custom Vision - Image Prediction Test

This simple Python script allows you to **test a published Custom Vision model** using a local image. Perfect for AI-900 learners or anyone experimenting with Custom Vision predictions.

---

## ✅ Prerequisites

Make sure you have the following:

- A **trained and published** Azure Custom Vision project
- Your **Prediction Key**
- Your **Endpoint URL**
- Your **Project ID**
- Your **Published Model Name**
- A **local test image**

---

## 📦 Install Requirements

Install the required Python library:

```bash
pip install requests
```

---

## 🛠️ Configuration

Edit the script and replace the placeholders:

```python
prediction_key = "your_prediction_key_here"
endpoint = "https://<your-resource>.cognitiveservices.azure.com/"
project_id = "your_project_id_here"
published_name = "your_published_model_name"
image_path = r"path_to_your_test_image.jpg"
```

---

## 🚀 Run the Script

Run the Python script using:

```bash
python test.py
```

---

## 🖼️ Sample Output

```
✅ Predictions for orange_test.jpg:
🔹 orange: 97.25%
🔹 apple: 2.10%
🔹 banana: 0.20%
```

If there's an error:

```
❌ Prediction failed: 401
<Error details from Azure API>
```

---

## 📁 File Structure

```
📦 custom_vision_student_files/
├── config.py
├── main.py
├── test.py
├── README.md
└── test-images/
    └── orange_test.jpg
```

---

## 🙋 Need Help?

Make sure:
- The image path is valid
- All credentials are correctly copied from the Azure portal
- The model is published

Happy testing! 🎉
