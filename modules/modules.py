# Xương sống của ứng dụng
from data_io import read_account, write_account, read_car, write_car

# Lớp quản lý tài khoản người dùng
class AccountManage():
    def __init__(self):
        self.account_list = read_account()

    # Phương thức đăng nhập
    def login(self, username, password):
        for account in self.account_list:
            if account["username"] == username and account["password"] == password:
                return True # Thành công
        return False

    # Phương thức đăng ký
    def register(self, username, password, confirm):
        for account in self.account_list:
            if username == account["username"] or confirm != password:
                return False # Thất bại
        self.account_list.append({"username": username, "password": password})
        write_account(self.account_list)
        return True # Thành công

# Lớp định nghĩa đối tượng được quản lý
class CarInit():
    def __init__(self, model, brand, color, capacity):
        self.model = model
        self.brand = brand
        self.color = color
        self.capacity = capacity

# Lớp định nghĩa quản lý danh sách đối tượng ô tô
class CarManager():
    def __init__(self):
        self.car_list = list() # Danh sách rỗng chứa các ô tô cần quản lý
        self.car_list_dict = read_car() # Load dữ liệu từ json --> dictionary

    # Phương thức load dữ liệu và chuyển từ dict sang list
    def load_data(self):
        for car_dict in self.car_list_dict:
            car = CarInit(model = car_dict["model"],
                          brand = car_dict["brand"],
                          color = car_dict["color"],
                          capacity = car_dict["capacity"])
            self.car_list.append(car)

    # Phương thức tìm đối tượng thông qua thuộc tính model --> Sửa, xóa đối tượng đó
    def get_car_by_model(self, model):
        for car in self.car_list:
            if car.model == model:
                return car              # Nếu thấy --> Trả về đối tượng ô tô đó
        return None                     # Nếu không tìm thấy --> Trả về None

    # Phương thức thêm đối tượng ô tô
    def add_car(self, car_dict):
        car = CarInit(model = car_dict["model"],
                        brand = car_dict["brand"],
                        color = car_dict["color"],
                        capacity = car_dict["capacity"])
        self.car_list.append(car)
        self.car_list_dict.append(car_dict)
        write_car(self.car_list_dict)

    # Phương thức sửa đối tượng ô tô tìm được theo model
    def edit_car(self, car_model, new_car):
        # Tìm ô tô có model giống model được truyền vào
        matched = self.get_car_by_model(car_model)

        # Nếu tìm được
        if matched != None:
            # Thực hiện sửa dữ liệu dựa trên dữ liệu người dùng cập nhật vào
            matched.model = new_car.get("model", matched.model)
            matched.brand = new_car.get("brand", matched.brand)
            matched.color = new_car.get("color", matched.color)
            matched.capacity = new_car.get("capacity", matched.capacity)

        # Ghi dữ liệu vào json
        self.car_list_dict = [car.__dict__ for car in self.car_list]
        write_car(self.car_list_dict)

    # Phương thức xóa đối tượng ô tô tìm được theo model
    def delete_car(self, car_model):
        # Tìm ô tô có model giống model được truyền vào
        matched = self.get_car_by_model(car_model)

        # Nếu tìm thấy
        if matched != None:
            self.car_list.remove(matched) # Xóa ô tô tìm thấy
            # Cập nhật dữ liệu mới sau khi xóa vào json
            self.car_list_dict = [car.__dict__ for car in self.car_list]
            write_car(self.car_list_dict)

staff = CarManager()

print(staff.car_list)
staff.load_data()
print(staff.car_list)