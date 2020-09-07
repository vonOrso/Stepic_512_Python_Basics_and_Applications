# import sys, re
#
# for line in sys.stdin:
#     line = line.rstrip()
#     if len(re.findall('cat', line)) > 1:
#         print(line)

# import sys, re
#
# for line in sys.stdin:
#     line = line.rstrip()
#     if len(re.findall(r'\bcat\b', line)) > 0:
#         print(line)

# import sys, re
#
# for line in sys.stdin:
#     line = line.rstrip()
#     if len(re.findall(r'z\w\w\wz', line)) > 0:
#         print(line)

# import sys, re
#
# for line in sys.stdin:
#     line = line.rstrip()
#     if len(re.findall(r'\\', line)) > 0:
#         print(line)

# import sys, re
#
# for line in sys.stdin:
#     line = line.rstrip()
#     if len(re.findall(r'\b(\w+)\1\b', line)) > 0:
#         print(line)

# import sys, re
#
# for line in sys.stdin:
#     line = line.rstrip()
#     print(re.sub('human','computer',line))

# import sys, re
#
# for line in sys.stdin:
#     line = line.rstrip()
#     print(re.sub(r'\ba+\b','argh',line, flags = re.IGNORECASE, count=1))

# import sys, re
#
# for line in sys.stdin:
#     line = line.rstrip()
#     print(re.sub(r'\b(\w)(\w)', r'\2\1',line))

# import sys, re
#
# for line in sys.stdin:
#     line = line.rstrip()
#     print(re.sub(r'(\w)\1+', r'\1',line))

# import sys, re
#
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.fullmatch(r'[0|1]+', line):
#         lst = list(line)
#         chet, nechet = 0,0
#         for i in range(len(lst)):
#             if i % 2 == 0:
#                 chet += int(lst[i])
#             else:
#                 nechet += int(lst[i])
#         if (chet - nechet) % 3 == 0:
#             print(line)