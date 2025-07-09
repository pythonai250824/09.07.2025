

def get_x(a):
    return a.gap

class A:
    # class variable (static)
    a1 = [1] * 10_000  # static --> [1]

    def __init__(self):
        self.a2 = [1] * 10_000  # per-instance
        self.gap = 100

print(A.a1)
a1_instance = A()  # a1.a2 ref count = 1
a2_instance = A()  # a2.a2 ref count = 1
a3_instance = A()  # a3.a2 ref count = 1
b = a3_instance.a2.copy() # a2 ref count = 2
d = a3_instance.gap
del a3_instance  # a2 ref count = 1

print(get_x(a1_instance))

def func1(lx: list[int]) -> None:
    # 44 [2]
    x = 2
    func1(lx)
    lx.append(1)

l1 = [1] * 10_000  # 44  [1]

def f3(l4):
    # 55[2]
    l4.append(1)

def f2():
    l3 = [1] * 10_000 # 55 [1]
    f3(l3)
    # 55 [1]

# 55[0] -- cleaned from memory

func1(l1)
print(l1)
x = 1

def func2(y):
    y += 1

func2(x)
print(x)
