# Sorts a sequence in ascending order using the bubble sort algorithm.
def bubbleSort( theSeq ):
    n = len( theSeq )
    # Perform n-1 bubble operations on the sequence
    for i in range( 1,n ) :
        #print(i)
    # Bubble the largest item to the end.
        for j in range(0, n-i) :
            
            if theSeq[j] > theSeq[j + 1] :
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
        #print(theSeq)
    print(theSeq)
a=[1,5,4,8,0,12,35,43,67,9,81,11]
bubbleSort( a )
