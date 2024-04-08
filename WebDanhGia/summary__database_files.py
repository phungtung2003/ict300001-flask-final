import os
import json
import codecs

summary_dir = 'D:\ict300001 flask final\final product\Final\result\summary'
product_dir = 'D:\ict300001 flask final\final product\Final\product'
output_dir = 'D:\ict300001 flask final\final product\Final\summary'

# Tạo thư mục đầu ra nếu chưa tồn tại
os.makedirs(output_dir, exist_ok=True)

# Lặp qua tất cả các tệp JSON trong thư mục summary_dir
for filename in os.listdir(summary_dir):
    if filename.endswith('.json'):
        summary_path = os.path.join(summary_dir, filename)
        product_path = os.path.join(product_dir, filename)

        # Đọc dữ liệu từ tệp summary JSON
        with open(summary_path, 'r', encoding='utf-8') as summary_file:
            summary_data = json.load(summary_file)

        # Đọc dữ liệu từ tệp product JSON
        with open(product_path, 'r', encoding='utf-8') as product_file:
            product_data = json.load(product_file)

        # Kết hợp thông tin từ cả hai tệp JSON
        combined_data = {
            "file_name": summary_data['file_name'],
            "product_name": product_data['product_name'],
            "price": product_data['price'],
            "average_positive": summary_data['average_positive'],
            "average_negative": summary_data['average_negative'],
            "average_neutral": summary_data['average_neutral']
        }

        # Ghi thông tin vào tệp JSON đầu ra
        output_path = os.path.join(output_dir, filename)
        with codecs.open(output_path, 'w', encoding='utf-8') as output_file:
            json.dump(combined_data, output_file, indent=4, ensure_ascii=False)

print('Hoàn thành!')
