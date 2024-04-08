import torch
import json
import os
from transformers import RobertaForSequenceClassification, AutoTokenizer

model = RobertaForSequenceClassification.from_pretrained("wonrax/phobert-base-vietnamese-sentiment")
tokenizer = AutoTokenizer.from_pretrained("wonrax/phobert-base-vietnamese-sentiment", use_fast=False)

#Địa chỉ các thư mục sử dụng
input_directory = r"C:\Users\ngoqu\OneDrive\Máy tính\DuAnWeb\result\input"
output_directory = r"C:\Users\ngoqu\OneDrive\Máy tính\DuAnWeb\result\output"
summary_output_directory = r"C:\Users\ngoqu\OneDrive\Máy tính\DuAnWeb\result\final"

# Đảm bảo thư mục đầu ra tồn tại
os.makedirs(output_directory, exist_ok=True)
os.makedirs(summary_output_directory, exist_ok=True)

# Danh sách tên tệp JSON trong thư mục đầu vào
input_files = [f for f in os.listdir(input_directory) if f.endswith(".json")]

for input_file in input_files:
    input_file_path = os.path.join(input_directory, input_file)
    output_file_path = os.path.join(output_directory, input_file.replace(".json", "_output.json"))

    with open(input_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    output_data = []

    for item in data:
        review_no = item["review_no"]
        content = item["content"]

        input_ids = torch.tensor([tokenizer.encode(content)])

        with torch.no_grad():
            out = model(input_ids)
            positive = out.logits.softmax(dim=-1).tolist()[0][1]
            negative = out.logits.softmax(dim=-1).tolist()[0][0]
            neutral = out.logits.softmax(dim=-1).tolist()[0][2]
            
            output_item = {
                "file_name": input_file,  # Thêm tên tệp vào dữ liệu đầu ra
                "review_no": review_no,
                "positive": positive,
                "negative": negative,
                "neutral": neutral
            }

            output_data.append(output_item)
        
    # Ghi dữ liệu ra tệp JSON đầu ra
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        json.dump(output_data, output_file, ensure_ascii=False, indent=4)

    print("Output data saved to:", output_file_path)

# Tạo một danh sách tệp JSON đầu ra cho các tệp tổng kết
summary_output_files = []

for input_file in input_files:
    input_file_path = os.path.join(output_directory, input_file.replace(".json", "_output.json"))
    summary_output_file_path = os.path.join(summary_output_directory, input_file.replace(".json", "_summary.json"))

    with open(input_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    summary_data = {}

    total_positive = 0
    total_negative = 0
    total_neutral = 0
    total_reviews = len(data)
    
    for item in data:
        total_positive += item["positive"]
        total_negative += item["negative"]
        total_neutral += item["neutral"]

    average_positive = total_positive / total_reviews
    average_negative = total_negative / total_reviews
    average_neutral = total_neutral / total_reviews

    summary_data = {
        "file_name": input_file,  # Thêm tên tệp vào dữ liệu đầu ra
        "average_positive": average_positive,
        "average_negative": average_negative,
        "average_neutral": average_neutral
    }

    # Ghi dữ liệu tổng kết vào danh sách tệp tổng kết
    summary_output_files.append(summary_output_file_path)

    # Ghi dữ liệu tổng kết ra tệp JSON
    with open(summary_output_file_path, "w", encoding="utf-8") as summary_output_file:
        json.dump(summary_data, summary_output_file, ensure_ascii=False, indent=4)

    print("Summary output saved to:", summary_output_file_path)
