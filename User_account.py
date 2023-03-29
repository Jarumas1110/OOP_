class User_account:
    def __init__(self, id, email, tel, gender, password):
        self.id = id
        self.email = email
        self.tel = tel
        self.gender = gender
        self.password = password
        

    def login(self, id, password):
        if self.id == id and self.password == password:
            return True
        else:
            return False

    def change_password(self, new_password):
        self.password = new_password

    def change_tel(self, new_tel):
        self.tel = new_tel

users = []  #ลิสต์บัญชีผู้ใช้(ทุกคน)

def create_user():
    id = input("Enter id: ")
    email = input("Enter email: ")
    tel = input("Enter tel: ")
    gender = input("Enter gender: ")
    password = input("Enter password: ")
    user = User_account(id, email, tel, gender, password)
    users.append(user)
    print("User account created successfully.")

def login():
    id = input("Enter your id: ")
    password = input("Enter your password: ")
    for user in users:
        if user.login(id, password):
            print("Login successful.")
            return
    print("Incorrect id or password.")

def change_password():
    id = input("Enter your id: ")
    password = input("Enter your password: ")
    for user in users:
        if user.login(id, password):
            new_password = input("Enter your new password: ")
            user.change_password(new_password)
            print("Password changed successfully.")
            return
    print("Incorrect id or password.")

def change_tel():
    id = input("Enter your id: ")
    password = input("Enter your password: ")
    for user in users:
        if user.login(id, password):
            new_tel = input("Enter your new tel: ")
            user.change_tel(new_tel)
            print("Tel changed successfully.")
            return
    print("Incorrect id or password.")


# ตัวอย่างการใช้งานแต่ละฟังก์ชั่นคำสั่ง
create_user()
login()
change_password()
change_tel()
