
def lists_with_product_equal_n(lst):
    sublists = []
    length = len(lst)
 
    for i in range(length):
        j = (i + 1)%length
        product = lst[i]
        arr = [lst[i]]
        while product != -26 and j != i:
            product *= lst[j]
            arr.append(lst[j])
            if product == -26:
                sublists.append(arr.copy())
            j = (j + 1) % length
            if j == i:
                break
    return sublists
