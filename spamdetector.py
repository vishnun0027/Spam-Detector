import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
model = AutoModelForSequenceClassification.from_pretrained("vishnun0027/Spam-Detection")
tokenizer = AutoTokenizer.from_pretrained("vishnun0027/Spam-Detection")

# Check if GPU is available and set the device accordingly
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Move the model to the appropriate device
model.to(device)

def Detection(text:str):
    inputs = tokenizer(text, return_tensors="pt")
    inputs = {key: value.to(device) for key, value in inputs.items()}

    with torch.no_grad():
        logits = model(**inputs).logits
    predicted_class_id = logits.argmax().item()
    prediction = model.config.id2label[predicted_class_id]
    
    return prediction

# # Example usage
# text = """Omg you guyssss, have you heard about the new diet trend that's sweeping the nation?
# It's called the "Juice Cleanse" and it's soooooooo amazinggggg. All you have to do is drink
# juices made of fruits and vegetables for days and days and days and you'll lose like, a million
# pounds. Plus, it's super easy and you'll feel sooooo good about yourself. But wait, there's more! 
# Have you thought about trying out our new weight loss pills? They're made with all-natural ingredients 
# and will make you hot and skinny in no time. And don't worry
# """

# # Call the function
# result = Detection(text)
# print(f'Predicted class label: {result}')
