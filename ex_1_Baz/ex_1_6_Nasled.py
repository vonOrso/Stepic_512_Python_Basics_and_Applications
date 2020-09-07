# kk = {}
# for i in range(int(input())):
#     st = input().replace(':','').split(' ')
#     kk[st[0]] = st[2:]
# for i in range(int(input())):
#     st = input().split(' ')
#     if st[1] in kk.keys():
#         sp = [st[1]]
#         while sp!= []:
#             if sp[0]==st[0]:
#                 print('Yes')
#                 break
#             else:
#                 sp+=kk[sp[0]]
#                 sp.remove(sp[0])
#             if sp == []:
#                 print('No')
#     else:
#         print('No')

# class ExtendedStack(list):
#     def sum(self):
#         self.append(self.pop()+self.pop())
#     def sub(self):
#         self.append(self.pop()-self.pop())
#     def mul(self):
#         self.append(self.pop()*self.pop())
#     def div(self):
#         self.append(self.pop()//self.pop())

# # import time
# #
# # class Loggable:
# #     def log(self, msg):
# #         print(str(time.ctime()) + ": " + str(msg))
#
# class LoggableList(list, Loggable):
#     def append(self,obj):
#         super(LoggableList,self).append(obj)
#         self.log(obj)
