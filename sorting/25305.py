import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# 한 줄에 정수형으로 여러 수를 입력 받을 때
score = list(map(int, input().split()))
score.sort(reverse=True)  # 내림차순 정렬
print(score[k - 1])
