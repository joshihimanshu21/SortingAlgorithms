def cycle_sort(arr,n):
    global writes
    writes=0
    for cycle_start in range(0,n-1):
        item = arr[cycle_start]
        pos = cycle_start
        for i in range(cycle_start+1,n):
            if arr[i]<item:
                pos+=1
        if pos==cycle_start:
            continue
        while(item == arr[pos]):
            pos+=1
        if pos!=cycle_start:
            item,arr[pos]=arr[pos],item
            writes+=1
        while(pos!=cycle_start):
            pos=cycle_start
            for i in range(cycle_start+1,n):
                if arr[i]<item:
                    pos+=1
            while(item == arr[pos]):
                pos+=1
            if  item!=arr[pos]:
                item,arr[pos]=arr[pos],item
                writes+=1
n=int(input())
arr=list(map(int,input().split()))
cycle_sort(arr,n)
print(arr,writes)