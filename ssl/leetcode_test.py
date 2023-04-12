class Circle(object):
    pi = 3.14  # 类属性（每个实例共有的属性）

    # self 类实例（所有函数必有的参数）
    def __init__(self, r):  # 初始化一个属性
        self.r = r

    def get_area(self):  # 计算方法
        return self.pi*self.r**2

    def get_len(self):
        return 2*self.pi*self.r

    def __girth(self):  # 伪私有，只能在类内部访问该私有方法
        return 2*self.pi*self.r

    @classmethod
    def get_pi(cls):  # 类方法：不通过实例化就可以访问的方法
        return cls.pi


# 创建实例(r=1,r=2)
circle_one = Circle(1)
circle_two = Circle(2)
# 实例名.属性名---访问属性
print('访问实例属性：')
print(circle_one.r)
print(circle_two.r)
print('访问公有属性：')
print(Circle.pi)
print('计算圆的面积：')
print('半径r =', circle_one.r, '面积A =', circle_one.get_area())
print('半径r =', circle_two.r, '面积A =', circle_two.get_area())
print('计算圆周：')
print(circle_one.get_len())
print('不通过实例化访问类方法：', Circle.get_pi())


