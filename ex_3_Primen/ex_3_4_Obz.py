# import requests, re
#
# nachalo = input()
# poisk = input()
# sp = re.findall(r'https.+?html', str(requests.get(nachalo).content))
# nsp = []
# for i in sp:
#     nsp += re.findall(r'https.+?html', str(requests.get(i).content))
# print('Yes') if poisk in ' '.join(nsp) else print('No')

# import requests, re
# t = re.findall(r'''href=\\?['"](?:\w+?://)?.+?[/\\:'"]''', str(requests.get(input()).content))
# ss = sorted(set(map(lambda x: re.sub(r'''href=\\?['"](?:\w+?://)?''','',x[:-1]),t)))
# [print(i) for i in ss if i != '..' and i != 'pics.rbc.ru']
