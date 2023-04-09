# 숫자의 합
import sys
input = sys.stdin.readline

n = int(input())
str = input().split()
sum = 0
for ch in str[0]:
    sum += int(ch)
print(sum)

# print(sum(map(int, input())))
