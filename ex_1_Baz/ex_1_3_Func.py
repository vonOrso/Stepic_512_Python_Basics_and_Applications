# def closest_mod_5(x):
#     return x if x % 5 == 0 else x + (5 - (x - 5*(x//5)))

# def C(n,k):
#     if k == 0: return 1
#     elif k > n: return 0
#     else: return C(n-1,k)+ C(n - 1, k - 1)
#
# sp = input().split(' ')
# print(C(int(sp[0]),int(sp[1])))