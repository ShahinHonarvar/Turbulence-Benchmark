
def lists_with_product_equal_n(mylist, n):
    sublists = []
    for i in range(len(mylist)):
        for j in range(i+1, len(mylist)+1):
            if mylist[i:j].prod() == n:
                sublists.append(mylist[i:j])
    return sublists
