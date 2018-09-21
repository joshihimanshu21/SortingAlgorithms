def bubble_sort(arr):
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j+1]<arr[j]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
n=int(input())
arr = list(map(int,input().split()))
bubble_sort(arr)
print(arr)