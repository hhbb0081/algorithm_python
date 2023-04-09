# 부녀회장이 될테야
import sys
input = sys.stdin.readline

# 15 * 15의 이차원 배열 생성
dp = [[0] * 15] * 15

for i in range(1, 15):
    dp[0][i] = i

for i in range(15):
    dp[i][1] = 1

for i in range(1, 15):
    for j in range(1, 15):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    print(dp[k][n])
