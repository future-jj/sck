class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def study(self, hours):
        print(f"{self.name}学习了{hours}小时")
        
    def get_info(self):
        return f"姓名: {self.name}, 年龄：{self.age}, 年级：{self.grade}"
    
student1 = Student("张三", 18, "高三")
student2 = Student("李四", 17, "高二")


student1.study(2)
print(student1.get_info())


student2.study(3)
print(student1.get_info())

class BankAccount:
    def __init__(self, initial_balance = 0):
        self.__balance = initial_balance
        
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("存款金额必须大于0")
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("取金额必须大于0")
        if amount > self.__balance:
            raise ValueError("余额不足")
        
    def get_balance(self):
        return self.__balance
    
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())
try:
    account.deposit(-200)
except ValueError as e:
    print(e)
        
