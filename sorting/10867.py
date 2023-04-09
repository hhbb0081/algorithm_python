n = input('')
list = []
for i in range(0, int(n)):
    num = input('')
    list.append(int(num))
list.sort()

for num in list:
    print(num)
