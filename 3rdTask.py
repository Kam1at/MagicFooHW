class MyInt:
    def __init__(self, val):
        self.__val = val

    @classmethod
    def __check_data(cls, other):
        try:
            other = int(other)
        except:
            raise TypeError("Введите цифру")
        if not isinstance(other, (int, MyInt)):
            raise TypeError("Должен быть int или MyInt")
        return other if isinstance(other, int) else other.__val

    def __str__(self):
        return str(self.__val)

    def __add__(self, other):
        if isinstance(other, str):
            other = int(other)
        return MyInt(self.__val + other)

    def __radd__(self, other):
        if isinstance(other, str):
            other = int(other)
        return MyInt(self.__val + other)

    def __iadd__(self, other):
        if isinstance(other, str):
            other = int(other)
        self.__val = self.__val + other
        return self

    def __mul__(self, other):
        if isinstance(other, str):
            other = int(other)
        return MyInt(self.__val * other)

    def __rmul__(self, other):
        if isinstance(other, str):
            other = int(other)
        return MyInt(self.__val * other)

    def __imul__(self, other):
        if isinstance(other, str):
            other = int(other)
        self.__val = self.__val * other
        return self

    def __sub__(self, other):
        if isinstance(other, str):
            other = int(other)
        return MyInt(self.__val - other)

    def __rsub__(self, other):
        if isinstance(other, str):
            other = int(other)
        return MyInt(self.__val - other)

    def __isub__(self, other):
        if isinstance(other, str):
            other = int(other)
        self.__val = self.__val - other
        return self

    def __truediv__(self, other):
        if isinstance(other, str):
            other = int(other)
        return MyInt(self.__val / other)

    def __rtruediv__(self, other):
        if isinstance(other, str):
            other = int(other)
        return MyInt(self.__val / other)

    def __itruediv__(self, other):
        if isinstance(other, str):
            other = int(other)
        self.__val = self.__val / other
        return self

    def __eq__(self, other):
        oth = self.__check_data(other)
        return self.__val == oth

    def __lt__(self, other):
        oth = self.__check_data(other)
        return self.__val < oth

    def __ge__(self, other):
        oth = self.__check_data(other)
        return self.__val >= oth


a = MyInt(5)
# a = a + 5
# print(a)
# a = a - 2 - 3
# a = a * '5'
# print(a)
# a = a / 10
# print(a)
print(a < 3)
print(a >= "3")
print(a == '5')