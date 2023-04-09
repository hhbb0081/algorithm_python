import sys
input = sys.stdin.readline

# n 입력
n = int(input())
# 나이와 이름을 n만큼 입력받고 나이, 이름을 잘라 리스트에 담는다.
users = [list(input().split()) for _ in range(n)]

# 2차원 배열 행을 기준으로 하여 정렬
users.sort(key=lambda x: (int(x[0])))
# '나이 이름' 형태로 출력
for user in users:
    print(user[0] + ' ' + user[1])
