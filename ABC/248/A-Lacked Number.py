#AC

S = input()

list = []
for i in range(10):
    list.append(str(i))

for i in S:
  if i in list:
    list.remove(i)

print(list[0])