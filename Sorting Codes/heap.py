class heapsort(): ##heap sort class
    def downheaps(self, n):
        index=0
        left=index*2+1
        right=index*2+2
        while right<=n :
            if right+1<=n:
                if self.item[right]>=self.item[left] and self.item[index]<self.item[right]:
                    temp=self.item[index]
                    self.item[index]=self.item[right]
                    self.item[right]=temp
                    index=right
                    left=index*2+1
                    right=index*2+2
                elif self.item[index]<self.item[left] :
                    temp=self.item[index]
                    self.item[index]=self.item[left]
                    self.item[left]=temp
                    index=left
                    left=index*2+1
                    right=index*2+2
                else:
                    break
            elif self.item[index]<self.item[left] :
                    temp=self.item[index]
                    self.item[index]=self.item[left]
                    self.item[left]=temp
                    index=left
                    left=index*2+1
                    right=index*2+2
            else:
                break
    def sort(self):
        for i in range(len(self.item)-1,0, -1):
            temp=self.item[i]
            self.item[i]=self.item[0]
            self.item[0]=temp
            self.downheaps(i)


class heap(heapsort): ##heap class
    def __init__(self):
        self.item=[]
        
    def upheap(self,n):
        k=(n-1)//2
        while k>=0 and self.item[n]>self.item[k]:
            temp=self.item[k]
            self.item[k]=self.item[n]
            self.item[n]=temp
            n=k
            k=(k-1)//2

    def downheap(self):
        index=0
        n=len(self.item)
        left=index*2+1
        right=index*2+2
        while right<=n :
            if right+1<=n:#awlak. n-1 dala meetawada ketiyen karanna thibba
                if self.item[right]>=self.item[left] and self.item[index]<self.item[right]:
                    temp=self.item[index]
                    self.item[index]=self.item[right]
                    self.item[right]=temp
                    index=right
                    left=index*2+1
                    right=index*2+2
                elif self.item[index]<self.item[left] :
                    temp=self.item[index]
                    self.item[index]=self.item[left]
                    self.item[left]=temp
                    index=left
                    left=index*2+1
                    right=index*2+2
                else:
                    break
            elif self.item[index]<self.item[left] :
                    temp=self.item[index]
                    self.item[index]=self.item[left]
                    self.item[left]=temp
                    index=left
                    left=index*2+1
                    right=index*2+2
            else:
                break
                    
            
    def add (self, poo):
        self.item.append(poo)
        n=len(self.item)-1
        self.upheap(n)

    def remove(self):
        n=len(self.item)-1
        largest_item=self.item[0]
        end_item=self.item[n]
        self.item[0]=end_item
        self.item[n]=largest_item
        k=self.item.pop(n)
        self.downheap()
        return k

    
a=heap()

import random
for x in range(0,33):
    n=random.randrange(70)
    a.add(n)
print(a.item)
a.remove()
print(a.item)
a.sort()
print(a.item)
