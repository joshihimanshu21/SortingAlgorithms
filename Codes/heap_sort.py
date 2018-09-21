from random import  sample
def left(i):
    return 2*i+1
def right(i):
    return 2*i+2
def min_heapify(A,i):
    l=left(i)
    r=right(i)
    if l<len(A) and A[l]<A[i]:
        smallest=l
    else:
        smallest=i
    if r<len(A) and A[r]<A[smallest]:
        smallest=r
    if smallest!=i:
        A[i],A[smallest]=A[smallest],A[i]
        min_heapify(A,smallest)
def built_min_heap(A):
    for i in range(len(A)//2,-1,-1):
        min_heapify(A,i)

def heap_sort(A):
    for i in range(len(A)):
        built_min_heap(A)
        print(A[0])
        A[0]=A[-1]
        del A[0]
A=sample(range(0,10000),10)
print(A)
heap_sort(A)