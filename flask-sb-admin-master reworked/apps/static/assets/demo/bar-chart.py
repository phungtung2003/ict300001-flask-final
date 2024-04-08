import time
import re

js_file_path = 'chart-bar-demo.js'  # Đường dẫn đến tệp JavaScript
data_file_path = 'bar-chart.txt'            # Đường dẫn đến tệp chứa dữ liệu mới

# Hàm cập nhật các giá trị dữ liệu trong mã JavaScript
def update_data_values(js_code, data_values):
    # Định nghĩa các biểu thức chính quy để tìm và thay thế các giá trị dữ liệu trong datasets
    data_regex = r'data:\s*\[([\d.,\s]+)\]\s*'
    updated_code = re.sub(data_regex, f'data: {str(data_values)}', js_code)
    return updated_code

# Vòng lặp để cập nhật mã JavaScript mỗi 1 giây
while True:
    # Đọc dữ liệu từ tệp
    with open(data_file_path, 'r') as file:
        data = file.read().strip()

    # Chia dữ liệu thành các giá trị riêng lẻ
    data_values = [float(value) for value in data.split(',')]

    # Đọc mã JavaScript từ tệp
    with open(js_file_path, 'r') as file:
        js_code = file.read()

    # Cập nhật các giá trị dữ liệu trong mã JavaScript
    updated_js_code = update_data_values(js_code, data_values)

    # Ghi lại mã JavaScript đã được cập nhật vào tệp
    with open(js_file_path, 'w') as file:
        file.write(updated_js_code)

    time.sleep(1)  # Chờ 1 giây trước khi lặp lại quá trình
