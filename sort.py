def Sort(listone):
    for num in range(len(listone)-1,0,-1):
        for x in range(num):
            if listone[x]>listone[x+1]:
                s = listone[x]
                listone[x] = listone[x+1]
                listone[x+1] = s

listone = [67,45,2,13,1,998]
Sort(listone)
print(listone)

''' SECOND SORT
def Sort2(listtwo):
    for num in range(len(listtwo)-1,0,-1):
        for x in range(num):
            if listtwo[x]>listtwo[x+1]:
                s = listtwo[x]
                listtwo[x] = listtwo[x+1]
                listtwo[x+1] = s

listtwo = [89,23,33,45,10,12,45,45,45]
Sort2(listtwo)
print(listtwo)
'''
