# fib = lambda x : 1 if x <= 2 else fib(x - 1) + fib(x - 2)
# print(fib(31))

# x = [1, 2, 3]
# y = x
# y.append(4)
# s = "123"
# t = s
# t = t + "4"
# print(str(x) + " " + s)

# a = []
# def foo(arg1, arg2):
#   a.append("foo")
# foo(a.append("arg1"), a.append("arg2"))
# print(a)

# def h():
#   print(12)
#
# def f():
#   g(h)
#
# def g(a):
#   a()
#
# g(f)

# def s(a, *vs, b=10):
#    res = a + b
#    for v in vs:
#        res += v
#    return res
# #print(s(5, 5, 5, 5, 1))
# #print(s(21))
# # print(s(11, 10, b=10))
# # print(s(11, b=20))
# # print(s(11, 10))

# x, y = 1, 2
# def foo():
#     global y
#     if y == 2:
#         x = 2
#         y = 1
# foo()
# print(x)
# if y == 1:
#     x = 3
# print(x)

# class A:
#     def __init__(self, val=0):
#         self.val = val
#
#     def add(self, x):
#         self.val += x
#
#     def print_val(self):
#         print(self.val)
#
#
# a = A()
# b = A(2)
# c = A(4)
# a.add(2)
# b.add(2)
#
# a.print_val()
# b.print_val()
# c.print_val()

# class A:
#     val = 1
#
#     def foo(self):
#         A.val += 2
#
#     def bar(self):
#         self.val += 1
#
#
# a = A()
# b = A()
#
# a.bar()
# a.foo()
#
# c = A()
#
# print(a.val)
# print(b.val)
# print(c.val)

# class Base:
#     def __init__(self):
#         self.val = 0
#
#     def add_one(self):
#         self.val += 1
#
#     def add_many(self, x):
#         for i in range(x):
#             self.add_one()
#
# class Derived(Base):
#     def add_one(self):
#         self.val += 10
#
#
# a = Derived()
# a.add_one()
#
# b = Derived()
# b.add_many(3)
#
# print(a.val)
# print(b.val)

# class A:
#    def foo(self):
#       print("A")
#
# class B(A):
#    pass
#
# class C(A):
#    def foo(self):
#       print("C")
#
# class D:
#    def foo(self):
#       print("D")
#
# class E(B, C, D):
#    pass
#
# E().foo()

# class A:
#     pass
#
# class B(A):
#     pass
#
# class C:
#     pass
#
# class D(C):
#     pass
#
# class E(B, C, D):
#     pass

class Any:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        for i in self.iterable:
            if i != 2:
                yield i


list_a = [1, 2, 3,4,5,6,7,8,9]
obj = Any(list_a)
list_b = list(obj)

print(list_a)
print(obj)
print(list_b)