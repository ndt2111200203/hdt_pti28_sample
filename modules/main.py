# Dùng để lập trình tương tác giữa logic ứng dụng và giao diện ứng dụng

# Khai báo các thư viện cần thiết
from PyQt6 import QtCore
import sys
import os
import PyQt6.QtWidgets as QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic

# Nhập các modules cần thiết từ các file khác
import modules, dialog

# Khai báo đường dẫn tổng của project
BASE_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# Khai báo đường dẫn con
START_PATH = os.path.join(BASE_PATH, 'ui', 'start.ui')
MAIN_PATH = os.path.join(BASE_PATH, 'ui', 'main.ui')

# Class xử lý giao diện Đăng nhập - Đăng ký
class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(START_PATH, self)
        self.account_manager = modules.AccountManage()

        # Các events click button
        self.lg_login.clicked.connect(self.login)         # ĐN
        self.lg_gotoreg.clicked.connect(self.gotoreg)     # Sang trang ĐK
        self.rg_register.clicked.connect(self.register)   # ĐK
        self.rg_gotolog.clicked.connect(self.gotolog)     # Sang trang ĐN

    # Phương thức xử lý events đăng nhập
    def login(self):
        username = self.lg_username.text()
        password = self.lg_password.text()
        result = self.account_manager.login(username, password)
        if result == True:
            QMessageBox.information(self, "Success", "Đăng nhập thành công")
            # Mở trang chủ
            main.show()
            self.close()
        else:
            QMessageBox.warning(self, "Failed", "Đăng nhập thất bại")

    # Phương thức xử lý events đăng ký
    def register(self):
        username = self.rg_username.text()
        password = self.rg_password.text()
        confirm = self.rg_confirm.text()
        result = self.account_manager.register(username, password, confirm)
        if result == True:
            QMessageBox.information(self, "Success", "Đăng ký thành công")
            self.stackedWidget.setCurrentIndex(0)
        else:
            QMessageBox.warning(self, "Failed", "Đăng ký thất bại")

    # Phương thức xử lý events chuyển trang đăng ký
    def gotoreg(self):
        self.stackedWidget.setCurrentIndex(1)

    # Phương thức xử lý events chuyển trang đăng nhập
    def gotolog(self):
        self.stackedWidget.setCurrentIndex(0)

# Class xử lý giao diện trang chủ
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(MAIN_PATH, self)

        # Tạo đối tượng quản lý danh sách car
        self.car_manager = modules.CarManager()
        self.car_manager.load_data()

        # Các events click button
        self.m_add.clicked.connect(self.add)         # Thêm
        self.m_edit.clicked.connect(self.edit)       # Sửa
        self.m_delete.clicked.connect(self.delete)   # Xóa

    # Phương thức thêm đối tượng
    def add(self):
        dialog_add = dialog.Dialog()

        if dialog_add.exec():
            inputs = dialog_add.return_data_add() # lấy dữ liệu người dùng nhập vào
            self.listWidgets.addItem(inputs["model"]) # Thêm dữ liệu vào danh sách hiển thị
            self.car_manager.add_car(inputs) # Thêm dữ liệu vào json

    # Phương thức sửa đối tượng
    def edit(self):
        pass

    # Phương thức xóa đối tượng
    def delete(self):
        pass

# Hàm main chạy chương trình
if __name__ == '__main__':
    app = QApplication(sys.argv)
    start = StartWindow()
    main = MainWindow()
    start.show()
    sys.exit(app.exec())
