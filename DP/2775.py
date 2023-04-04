# 부녀회장이 될테야
import sys
input = sys.stdin.readline

# 15 * 15의 이차원 배열 생성
dp = [[0] * 15] * 15

for i in range(15):
    dp[0][i] = i + 1

t = int(input())
for _ in range(t):
    n = int(input())
    k = int(input())
    for i in range(0, k):
        for j in range(1, n + 1):
            dp[i][j] += dp[i][j - 1]
    print(dp[k - 1][n])
