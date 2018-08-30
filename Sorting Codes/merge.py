# Merges two sorted lists to create and return a new sorted list.
def mergeSortedLists( listA, listB ) :
# Create the new list and initialize the list markers.
    newList = list()
    a = 0
    b = 0
# Merge the two lists together until one is empty.
    while a < len( listA ) and b < len( listB ) :
        if listA[a] < listB[b] :
            newList.append( listA[a] )
            a += 1
        else :
            newList.append( listB[b] )
            b += 1
# If listA contains more items, append them to newList.
    while a < len( listA ) :
        newList.append( listA[a] )
        a += 1
# Or if listB contains more items, append them to newList.
    while b < len( listB ) :
        newList.append( listB[b] )
        b += 1
    return newList
 # Sorts a Python list in ascending order using the merge sort algorithm.
def pythonMergeSort( theList ):
 # Check the base case - the list contains a single item.
     if len(theList) <= 1 :
         return theList
     else :
 # Compute the midpoint.
         mid = len(theList) // 2

 # Split the list and perform the recursive step.
         leftHalf = pythonMergeSort( theList[ :mid ] )
         rightHalf = pythonMergeSort( theList[ mid: ] )

 #Merge the two ordered sublists.
         newList = mergeSortedLists( leftHalf, rightHalf )
         return newList
print(pythonMergeSort( [3,1,5,2,9,50,78,34,16,61] ))
