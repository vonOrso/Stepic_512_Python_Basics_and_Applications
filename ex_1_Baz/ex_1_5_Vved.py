# class MoneyBox:
#     def __init__(self, capacity=0):
#         self.capacity = capacity
#     def can_add(self, v):
#         return True if v <= self.capacity else False
#     def add(self, v):
#         if self.can_add(v) == True:
#             self.capacity -= v
#             return self.capacity
#         else:
#             return self.capacity

# class Buffer:
#     def __init__(self):
#         self.sp = []
#
#     def add(self, *a):
#         for i in a:
#             self.sp.append(i)
#             if len(self.sp) == 5:
#                 print(sum(self.sp))
#                 self.sp = []
#
#     def get_current_part(self):
#         return self.sp