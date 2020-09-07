# with open('dataset_24465_4.txt') as lns, open('ans_dataset_24465_4.txt','w') as wr:
#     lns = list(lns)
#     for i in range(len(lns)):
#         wr.write(lns.pop())

# import os.path
# sp = []
# for curr_dir,dirs,fls in os.walk('main'):
#     [sp.append(curr_dir) for i in fls if i[-3:] == '.py']
# [print(sp[i]) for i in range(len(sp)) if sp[i]!=sp[i-1]]