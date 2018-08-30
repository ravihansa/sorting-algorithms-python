def selsrt (lst):
    n=len(lst)
    for i in range (0, n):
        k=small(i, lst)
        temp=lst[i]
        lst[i]=lst[k]
        lst[k]=temp
    print(lst)
def small(fst, lst):
    val=lst[fst]
    ind=fst
    for x in range (fst, len(lst)):
        if lst[x]<val:
            val=lst[x]
            ind=x
    #print(val)
    return ind
a=[1,5,4,8,0,12,35,43,1,67,9,81,11]
selsrt(a)
