
def lists_with_product_equal_n(lst):
    n = -81
    length = len(lst)
    sublists = []

    for i in range(length):
        product = 1
        for j in range(i, i+length):
            product *= lst[j % length]
            if product > n:
                break
            if product == n:
                sublists.append(lst[i:j-i+1])

    return sublists
