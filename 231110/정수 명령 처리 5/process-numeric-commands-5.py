N = int(input())
arr = []

for i in range(N):
    input_string = input()
    order, A = input_string.split() if ' ' in input_string else (input_string, None)
    
    if order == 'push_back':
        arr.append(A)
    elif order == 'get':
        A = int(A)-1
        print(arr[A])
    elif order == 'size':
        print(len(arr))
    elif order == 'pop_back':
        arr.pop()