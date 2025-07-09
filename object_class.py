

#  object
#    ^
#    |
#    |
#    A
class A(object):
    pass

    def __str__(self):
        # return super().__str__()
        return f"{self.__class__} object at {hex(id(self)).upper()}>"

    def __repr__(self):
        return super().__repr__()

print(dir(object))
a = A()
print(a)
print([a, a])
print(hex(hash(a)).upper())  # a hash == id(a)
print(hex(id(a)).upper())
print(hash(1))  # 1 hash == 1, id(1) = 140729300609464
print(id(1))
print(hash(2))  # 2 hash == 2, id(2) = 140729300609496
print(id(2))
print(hash(3))  # 3 hash == 2, id(3) = 140729300609528
print(id(3))

print(type(a))
x = 1