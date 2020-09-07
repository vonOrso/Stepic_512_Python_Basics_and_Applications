# try:
#     foo()
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# except ArithmeticError:
#     print("ArithmeticError")
# except AssertionError:
#     print("AssertionError")

# nasled = {}
# for i in range(int(input())):
#     st = input().replace(':', '').split(' ')
#     if len(st) > 1:
#         nasled[st[0]] = st[2:]
# sp = []
# for i in range(int(input())):
#     zn = input()
#     if zn in sp:
#         print(zn)
#         continue
#     sp.append(zn)
#     if zn in nasled.keys():
#         prov = nasled[sp[-1]].copy()
#         while prov != []:
#             if prov[0] in sp:
#                 print(zn)
#                 break
#             else:
#                 if prov[0] in nasled.keys(): prov+=nasled[prov[0]]
#                 prov.remove(prov[0])

# class NonPositiveError(Exception):
#     pass
#
# class PositiveList(list):
#     def append(self,obj):
#         if obj>0:
#             super(PositiveList, self).append(obj)
#         else:
#             raise NonPositiveError