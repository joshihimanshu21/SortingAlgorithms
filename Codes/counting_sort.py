from random import sample
def countsort(arr):
    n=len(arr)
    maxval=max(arr)
    m=maxval+1
    count=[0]*m
    for a in arr:
        count[a]+=1
    i=0
    for a in range(m):
        for c in range(count[a]):
            arr[i]=a
            i+=1
    return arr
arr=list(map(int,input().split()))
#arr=sample(range(1000),1000)
#print(len(arr))
#print(arr)
print(countsort(arr))