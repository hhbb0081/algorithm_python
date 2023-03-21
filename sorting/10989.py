import sys
# 입력 시간 줄이기
input = sys.stdin.readline
n = int(input())

# 입력 값 중 최댓 값
Max = 0

# list에 미리 메모리 할당
List = [0] * 10001

for i in range(0, n):
    num = int(input())
    List[num - 1] += 1

    # 최댓값 구하기
    if Max < num:
        Max = num

for i in range(Max):
    # 해당 숫자가 존재하면
    if List[i] != 0:
      # 해당 숫자 개수만큼 출력
        for j in range(List[i]):
            print(i + 1)
