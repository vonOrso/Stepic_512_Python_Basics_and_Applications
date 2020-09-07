d = {'global': {'parent': 'None', 'vars': []}}
for i in range(int(input())):
    st = input().split(' ')
    if st[0] == 'create':
        d[st[1]] = {'parent': st[2], 'vars': []}
    elif st[0] == 'add':
        d[st[1]]['vars'].append(st[2])
    elif st[0] == 'get':
        if st[1] not in d.keys():
            print('None')
        else:
            t = st[1]
            while t != 'None':
                if st[2] in d[t]['vars']:
                    print(t)
                    break
                t = d[t]['parent']
            if t == 'None': print('None')