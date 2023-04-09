# 막대기
import sys
input = sys.stdin.readline
n = int(input())

stack = []
for i in range(n):
    stack.append(int(input()))

# 맨 마지막 수가 높이 최댓값
Max = stack[-1]
ans = 1
for hei in stack[::-1]:
    # 최댓값보다 큰 경우만 답 갱신
    if Max < hei:
        ans += 1
        Max = hei
print(ans)
