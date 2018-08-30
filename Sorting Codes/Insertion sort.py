def insertionSort( theSeq ):
    n = len( theSeq )
    for i in range( 1, n ) :

        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos - 1] :
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        theSeq[pos] = value
        #print (theSeq)
    print (theSeq)
a=[2,1,0,5,4,7,3,9,6]
insertionSort( a )
