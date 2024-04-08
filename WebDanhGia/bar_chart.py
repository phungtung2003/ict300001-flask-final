import os
import json

json_dir = 'C:/Users/ngoqu/flask-dashboard-sb-admin/apps/static/assets/Database/growth'
output_dir = 'C:/Users/ngoqu/flask-dashboard-sb-admin/apps/static/assets/Database/bar_chart_text_files'

# Lặp qua tất cả các tệp JSON trong thư mục json_dir
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        json_path = os.path.join(json_dir, filename)

        # Đọc dữ liệu từ tệp JSON
        with open(json_path, 'r') as file:
            data = json.load(file)

        # Trích xuất thông tin pos, neg, neu
        pos = data['average_positive']
        neg = data['average_negative']
        neu = data['average_neutral']

        # Tạo đường dẫn và tên tệp văn bản đầu ra
        output_filename = os.path.join(output_dir, os.path.splitext(filename)[0] + '.txt')

        # Ghi thông tin pos, neg, neu vào tệp văn bản
        with open(output_filename, 'w') as file:
            file.write(f"{pos},{neg},{neu}")
        print ("Trích xuất dữ liệu thành công")
