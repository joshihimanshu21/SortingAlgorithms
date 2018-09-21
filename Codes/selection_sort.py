def selection_sort1(arr):
    for i in range(0,n):
        small=arr[i]
        pos=i
        for j in range(i+1,n):
            if arr[j]<small:
                small=arr[j]
                pos=j
        arr[pos]=arr[i]
        arr[i]=small
n=int(input())
arr=list(map(int,input().split()))
selection_sort1(arr)
print(arr)