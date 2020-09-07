# from datetime import date, timedelta
# dt = input().split(' ')
# ndt = date(day=int(dt[2]), month= int(dt[1]), year=int(dt[0]))+timedelta(days = int(input()))
# print(ndt.year,ndt.month,ndt.day)

# # установка пакета, что бы работало на шиндовсе: pip install simple-crypt --no-dependencies
# # requests ставится нормально: pip/conda install requests
# # если гемор не нужен, ответ: Alice loves Bob
# import requests
# from simplecrypt import decrypt, DecryptionException
# encrypted = requests.get('https://stepic.org/media/attachments/lesson/24466/encrypted.bin').content
# passwords = requests.get('https://stepic.org/media/attachments/lesson/24466/passwords.txt').content
#
# for p in passwords.split():
#     try:
#         s = decrypt(p, encrypted)
#     except DecryptionException:
#         pass
#     else:
#         print(s)

