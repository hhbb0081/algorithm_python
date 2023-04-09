import sys
input = sys.stdin.readline

num = input().split()

num_list = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
            5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
            'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
            'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
m = int(num[0])
n = int(num[1])

ans = []
for i in range(m, n + 1):
    if i < 10:
        ans.append(num_list[i])
    else:
        str = num_list[i // 10] + ' ' + num_list[i % 10]
        ans.append(str)

ans.sort()
cnt = 0
for engNum in ans:
    cnt += 1
    if cnt % 10 != 0:
        engNum = engNum.split(" ")
        if len(engNum) == 1:
            print(num_list[engNum[0]], end=" ")
        else:
            print(num_list[engNum[0]] +
                  num_list[engNum[1]], end=" ")
    else:
        engNum = engNum.split(" ")
        if len(engNum) == 1:
            print(num_list[engNum[0]])
        else:
            print(num_list[engNum[0]] +
                  num_list[engNum[1]])
