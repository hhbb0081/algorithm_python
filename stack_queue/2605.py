import sys

input = sys.stdin.readline
n = int(input())
order = list(map(int, input().split()))

ans = []
now = 1
for i in order:
    ans.insert(now - i - 1, now)
    now += 1
for num in ans:
    print(num, end=' ')
