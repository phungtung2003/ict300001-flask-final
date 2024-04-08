import torch
from transformers import RobertaForSequenceClassification, AutoTokenizer

# Load pre-trained model and tokenizer
model = RobertaForSequenceClassification.from_pretrained("wonrax/phobert-base-vietnamese-sentiment")
tokenizer = AutoTokenizer.from_pretrained("wonrax/phobert-base-vietnamese-sentiment", use_fast=False)

# Function to evaluate sentiment
def evaluate_sentiment(input_text):
    # Tokenize input text
    input_ids = torch.tensor([tokenizer.encode(input_text)])
    
    # Perform inference
    with torch.no_grad():
        output = model(input_ids)
        probabilities = output.logits.softmax(dim=-1).tolist()[0]
    
    # Print probabilities for each sentiment class
    print("Sentiment probabilities:", probabilities)
    
    # Determine the predicted sentiment
    labels = ["Negative", "Positive", "Neutral"]
    predicted_sentiment = labels[probabilities.index(max(probabilities))]
    
    return predicted_sentiment

# Input from user
input_text = input("Nhập câu bạn muốn đánh giá cảm xúc: ")

# Evaluate sentiment
predicted_sentiment = evaluate_sentiment(input_text)
print("Cảm xúc dự đoán:", predicted_sentiment)
