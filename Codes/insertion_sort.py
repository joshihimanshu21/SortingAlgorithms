def insertion_sort1(arr):
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
n=int(input())
arr=list(map(int,input().split()))
insertion_sort1(arr)
print(arr)