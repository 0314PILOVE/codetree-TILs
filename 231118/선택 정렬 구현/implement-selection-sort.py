n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    min = i
    for j in range(i+1, n, 1):
        if arr[min] > arr[j]:
            min = j
    temp = arr[i]
    arr[i] = arr[min]
    arr[min] = temp

for i in range(n):
    print(arr[i], end=' ')