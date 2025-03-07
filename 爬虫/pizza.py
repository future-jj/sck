class Pizza:
    size_options = {"S", "M", "L"}
    def __init__(self, size, toppings = None):
        self.validate_size(size)
        self.size = size
        self.toppings = toppings if toppings is not None else []
        
    @classmethod
    def validate_size(cls, size):
        if size not in cls.size_options:
            raise ValueError(f"无效尺寸：{size}，可用尺寸：{cls.size_options}")
    
    @staticmethod    
    def calculate_price(size, toppings_count):
        Pizza.validate_size(size)  #复用验证逻辑
        base_prices = {"S":10, "M":12, "L":14}
        return base_prices[size] + toppings_count * 2
    
    def get_price(self):
        return Pizza.calculate_price(self.size, len(self.toppings))

# 创建披萨对象
p1 = Pizza("S", ["cheese", "mushroom"])
p2 = Pizza("M", ["pepperoni"])
p3 = Pizza("L")  # 空配料

# 通过静态方法直接计算
print(Pizza.calculate_price("S", 2))  # 输出：14 (10 + 2*2)

# 通过实例方法获取价格
print(f"S号披萨价格：{p1.get_price()}")  # 输出：14
print(f"M号披萨价格：{p2.get_price()}")  # 输出：14 (12 + 1*2)
print(f"L号披萨价格：{p3.get_price()}")  # 输出：14 (14 + 0)

# 非法尺寸测试
try:
    Pizza("XL")  # 触发异常
except ValueError as e:
    print(e)  # 输出：无效尺寸：XL，可用尺寸：['S', 'M', 'L']