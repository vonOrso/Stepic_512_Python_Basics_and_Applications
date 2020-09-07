objects = [1, 2, 1, 2, 3]
spis = [objects[0]]
for i in range(1,len(objects)):
    if objects[i] not in spis and objects[i-1] is not objects[i]: spis.append(objects[i])
print(len(spis))