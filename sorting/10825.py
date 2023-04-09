import sys
input = sys.stdin.readline

n = int(input())

# 입력 받고 split 한 후 리스트로 변환하는 것을 n번만큼 반복
stu_list = [list(sys.stdin.readline().split()) for _ in range(n)]

# 국어 내림차순, 영어 오름차순, 수학 내림차순, 이름 오름차순
stu_list.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in stu_list:
    print(student[0])
