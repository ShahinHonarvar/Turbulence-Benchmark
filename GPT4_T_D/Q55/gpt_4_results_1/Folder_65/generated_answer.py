
def lists_with_product_equal_n(lst):
    n = 46
    length = len(lst)
    sublists = []
    for i in range(length):
        for j in range(i, i+length):
            sublist = lst[j%length:(j+i+1)%length]
            product = 1
            for number in sublist:
                product *= number
            if product == n:
                sublists.append(sublist)
    return sublists
