import sys
input = sys.stdin.readline

n, k = map(int, input().split())

List = list(map(int, input().split()))
List.sort()
print(List[k - 1])
