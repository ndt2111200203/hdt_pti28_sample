# Đọc - Ghi dữ liệu vào trong file json
import json
import os

# Khai báo đường dẫn tổng của project
BASE_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# Khai báo đường dẫn con
ACCOUNT_PATH = os.path.join(BASE_PATH, 'data', 'accounts.json')
CAR_PATH = os.path.join(BASE_PATH, 'data', 'car.json')

# Hàm read dữ liệu từ json account
def read_account():
    with open(ACCOUNT_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

# Hàm write dữ liệu từ json account
def write_account(data):
    with open(ACCOUNT_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Hàm read dữ liệu từ json car
def read_car():
    with open(CAR_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

# Hàm write dữ liệu từ json car
def write_car(data):
    with open(CAR_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)