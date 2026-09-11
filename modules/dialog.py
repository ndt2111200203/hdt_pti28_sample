import os
from PyQt6 import uic
from PyQt6.QtWidgets import QDialog

# Khai báo đường dẫn tổng của project
BASE_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# Khai báo đường dẫn con
DIALOG_PATH = os.path.join(BASE_PATH, 'ui', 'dialog.ui')

# Class xử lý giao diện Dialog
class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(DIALOG_PATH, self)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    # Phương thức trả về dữ liệu khi thêm car
    def return_data_add(self) -> dict:
        return {
            "model": self.add_model.text(),
            "brand": self.add_brand.text(),
            "color": self.add_color.text(),
            "capacity": self.add_capacity.text()
        }

    # Phương thức trả về dữ liệu khi sửa car
    def return_data_edit(self) -> dict:
        return {
            "model": self.edit_model.text(),
            "brand": self.edit_brand.text(),
            "color": self.edit_color.text(),
            "capacity": self.edit_capacity.text()
        }

    # Phương thức hiển thị dữ liệu khi sửa car
    def show_data_edit(self, car):
        self.edit_model.setText(car.model)
        self.edit_brand.setText(car.brand)
        self.edit_color.setText(car.color)
        self.edit_capacity.setText(car.capacity)