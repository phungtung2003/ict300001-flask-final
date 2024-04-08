import json
import os
import codecs

summary_output_directory = r"D:\ict300001 flask final\final product\Final\result\summary"
final_output_directory = r"D:\ict300001 flask final\final product\Final\result\index"

# Tạo danh sách các tệp tổng kết
summary_files = [f for f in os.listdir(summary_output_directory) if f.endswith("_summary.json")]

total_positive = 0
total_negative = 0
total_neutral = 0
total_reviews = 0

# Tính tổng các thông số từ các tệp tổng kết
for summary_file in summary_files:
    summary_file_path = os.path.join(summary_output_directory, summary_file)

    with open(summary_file_path, "r", encoding="utf-8") as file:
        summary_data = json.load(file)

    total_positive += summary_data["average_positive"]
    total_negative += summary_data["average_negative"]
    total_neutral += summary_data["average_neutral"]
    total_reviews += 1

# Tính trung bình tổng
average_positive = total_positive / total_reviews
average_negative = total_negative / total_reviews
average_neutral = total_neutral / total_reviews

# Tạo dữ liệu cho tệp final
final_data = {
    "total_product_reviews": total_reviews,
    "average_positive": average_positive,
    "average_negative": average_negative,
    "average_neutral": average_neutral
}

final_output_file_name = "index_shop"

# Ghi dữ liệu ra tệp JSON final
final_output_file_path_json = os.path.join(final_output_directory, final_output_file_name + ".json")
with codecs.open(final_output_file_path_json, "w", encoding="utf-8") as final_output_file:
    json.dump(final_data, final_output_file, ensure_ascii=False, indent=4)
    
# Ghi dữ liệu ra tệp văn bản final
final_output_file_path_txt = os.path.join(final_output_directory, final_output_file_name + ".txt")
with codecs.open(final_output_file_path_txt, "w", encoding="utf-8") as final_output_file:    final_output_file.write(f"{average_positive},{average_negative},{average_neutral}")

print("Final output saved to:")
print(final_output_file_path_json)
print(final_output_file_path_txt)
