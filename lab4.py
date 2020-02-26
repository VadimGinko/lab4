from math import *


# Task1
class RangeIterableIterator:
    def __init__(self):
        self.x = 0
        print(self.x)
        self.y = 0
        print(self.y)
        self.z = 1
        print(self.z)
        self.size = 0
        pass

    # раз сам себе итератор - сам себя и возвращает
    def __iter__(self):
        return self

    def __next__(self):
        self.size += 1
        sim = self.x + self.y + self.z
        self.x = self.y
        self.y = self.z
        self.z = sim
        if self.size > 32:
            raise StopIteration
        return self.z

# Task2
class RangeIterableIterator2:

    def __init__(self):
        self.sum = 0
        self.i = 0
        self.x = 0
        self.sum_leibn = pi / 4
        pass

    # раз сам себе итератор - сам себя и возвращает
    def __iter__(self):
        return self

    def __next__(self):
        self.x = 1 / (2 * self.i + 1)
        if self.i % 2 == 0:
            self.sum += self.x
        else:
            self.sum -= self.x
        self.i += 1
        if round(fabs(self.sum - self.sum_leibn), 2) < 0.01:
            raise StopIteration
        return self.x


# Task1
print("тридцать пяти чисел трибоначчи: ")
iter1 = RangeIterableIterator()
for i in iter1:
    print(i)
print()

# Task2
iter2 = RangeIterableIterator2()
print("Числа ряда: ")
for i in iter2:
    print(i)
print("Сумма ряда: " + str(iter2.sum))