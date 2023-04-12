class Date(object):
    day = 0
    month = 0
    year = 0

    # 重构init方法
    def __init__(self, year=0, month=0, day=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_str):
        year, month, day = date_str.split('-')
        # date = cls(year, month, day)
        date = cls(year, month, day)
        return date

    @staticmethod  # 静态方法：不强制传递类实例self参数，可以在类外访问的方法
    def is_date_valid(date_str):
        year, month, day = date_str.split('-')
        return int(year) <= 3999 and int(month) <= 12 and int(day) <= 31

    @property  # 将类方法转换为一个只读类属性（不可修改）
    def now(self):
        return 2022


# 类方法中使用cls，实例方法中使用self
date1 = Date.from_string('2023-04-12')
print(date1.year, date1.month, date1.day)
is_date = Date.is_date_valid('2023-04-12')
print('校验日期格式：', is_date)
print('类方法-->只读的类属性：', date1.now)