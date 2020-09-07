# import requests, csv
# from collections import Counter
#
# with requests.Session() as s:
#     decoded_content = s.get('https://stepic.org/media/attachments/lesson/24473/Crimes.csv').content.decode('utf-8')
#     csv_read = csv.DictReader(decoded_content.splitlines(), delimiter=',')
#     crimes = [row['Primary Type'] for row in csv_read if '2015' in row['Date']]
#     count = Counter(crimes)
#     print(count.most_common())

# import json
#
# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     for next in graph[start] - visited:
#         dfs(graph, next, visited)
#     return visited
#
# load = json.loads(input())
# alls = {i['name']: [] for i in load}
# for z in load:
#     for x in alls:
#         if x in z['parents']:
#             alls[x].append(z['name'])
#
# for el in alls:
#     alls[el] = set(alls[el])
#
# [print(element, ':', len(dfs(alls, element))) for element in sorted(alls.keys())]