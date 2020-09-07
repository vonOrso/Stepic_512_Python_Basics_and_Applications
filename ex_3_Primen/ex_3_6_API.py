# import requests
#
# with open('dataset_24476_3.txt') as txt:
#     txt = txt.read().split('\n')
#     for i in txt[:-1]:
#         with requests.Session() as s:
#             cont = s.get('http://numbersapi.com/'+i+'/math?json=true',timeout=5).content
#             print('Interesting') if 'found": true' in str(cont) else print('Boring')

# import requests, json
#
# token = 'ваш токен, в комментариях есть гайд по его получению'
# headers = {"X-Xapp-Token": token}
# with open('dataset_24476_4.txt') as txt:
#     txt = txt.read().split('\n')
#     sp = {}
#     bd = []
#     for i in txt[:-1]:
#         with requests.Session() as s:
#             cont = s.get('https://api.artsy.net/api/artists/' + i, headers=headers)
#             j = json.loads(cont.text)
#             s_name, b_day = j['sortable_name'], j['birthday']
#             if b_day in bd:
#                 sp[b_day] = sorted(sp[b_day] + [s_name])
#             else:
#                 bd.append(j['birthday'])
#                 sp[b_day] = [s_name]
#
#     for z in sorted(bd):
#         for x in sp[z]:
#             print(x)