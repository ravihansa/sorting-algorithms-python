def radixsort( lst ):
    digit=1
    column=10
    temp=0
    max=True
    while max:
        max=False
        binlst=[]
        for i in range (column):
            k=[]
            binlst.append(k)
        for num in lst:
            
            temp=num//digit
            binlst[temp%10].append(num)
            if temp>1:
                max=True
        l=0
        for i in binlst:
            for j in i:
                lst[l]=j
                l+=1
        digit*=column
        print(lst)
a=[23,5,67,14,23,9,67,4,3,5,32,75,86,35,324,7]
radixsort(a )
print(a)


            
