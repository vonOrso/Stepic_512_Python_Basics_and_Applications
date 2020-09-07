# class multifilter:
#     def judge_half(self,pos, neg):
#         return True if pos >= neg else False
#
#     def judge_any(self,pos, neg):
#         return True if pos >= 1 else False
#
#     def judge_all(self,pos, neg):
#         return True if neg == 0 else False
#
#     def __init__(self, iterable, *funcs, judge=judge_any):
#         self.iterable = iterable
#         self.funcs = funcs
#         self.judge = judge
#
#     def __iter__(self):
#         for i in self.iterable:
#             self.pos = 0
#             self.neg = 0
#             for z in self.funcs:
#                 if z(i) == True:
#                     self.pos +=1
#                 else:
#                     self.neg +=1
#             if self.judge(self,self.pos,self.neg)==True:
#                 yield i

# def primes():
#     num = 2
#     while True:
#         prime = True
#         for i in range(2, num):
#             if (num % i == 0):
#                 prime = False
#         if prime:
#             yield num
#         num+=1