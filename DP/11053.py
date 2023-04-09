# 가장 긴 증가하는 부분 수열
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * 1001
ans = 0
for i in range(n):
    for j in reversed(range(i)):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j] + 1, dp[i])
    ans = max(ans, dp[i])

print(ans + 1)
