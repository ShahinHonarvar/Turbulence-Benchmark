
def all_odd_ints_exclusive(lst):
    newList=[]
    for i in range(50,74):
        if lst[i]%2!=0:
            newList.append(lst[i])
    return newList
