n = int(input())
arr = list(map(int, input().split()))

for i in range(1, n):
    key = arr[i]    # 현재 요소
    j = i-1         # 이미 정렬된 부분의 마지막 인덱스

    # key보다 큰 값이면 오른쪽으로 한 칸씩 이동
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1

    arr[j+1] = key

for i in range(n):
    print(arr[i], end=' ')