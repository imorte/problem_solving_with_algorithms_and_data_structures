def findMin(alist):
    overallmin = alist[0]
    for i in alist:
        issmallest = True
        for j in alist:
            if i > j:
                issmallest = False
        if issmallest:
            overallmin = i

    return overallmin

print(findMin([5,4,2,1,0]))

def findMinSecond(alist):
    minsofar = alist[0]
    for i in alist:
        if i < minsofar:
            minsofar = i

    return minsofar

print(findMinSecond([5,1,2,3,5,3,0]))