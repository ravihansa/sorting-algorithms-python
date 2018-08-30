def Qsort(lst):
    if(len(lst)>1):
        srt(lst, 0, len(lst)-1)
    print(lst)

def srt (lst, first, last):
    
    if(last>first):
        #print(first)
        #print(last)
        pivot=lst[first]
        left=first+1
        right=last
        #print(left)
        #print(right)
        while(left<right):   
            while(lst[right]>=pivot and right !=first):
                right-=1
            
            while(lst[left]<pivot and left!=last):
                left+=1
            if left<right:
                k=lst[left]
                lst[left]=lst[right]
                lst[right]=k
        if lst[right]<pivot:
            temp=lst[right]
            lst[right]=pivot
            lst[first]=temp
        print(pivot)
        print(lst)
        srt (lst, first, right-1)
        srt (lst, right+1, last)
    
a=[2,5,3,7,9,8,2,4,567,23,956,7,4,23,68]
#a=[2,5,3,7,9,8,4,567,23,956,68]
Qsort(a)
