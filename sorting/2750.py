n = int(input())

# 입력받은 수들을 정수로 변환
inputList = list(map(int, input().split()))

# set으로 변환하여 중복 제거 후 다시 list로 변환
inputList = list(set(inputList))

# 정렬
inputList.sort()

# list의 값을 하나씩 출력
for num in inputList:
    # 줄 바꿈 문자를 제거하기 위해 end 매개변수 사용
    print(num, end=" ")
