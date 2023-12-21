
def lists_with_product_equal_n(lst):
    sublists = []
    size = len(lst)
    for i in range(size):
        for j in range(i, size):
            sublist = lst[i:j] + lst[:j-i] if j < i else lst[i:j+1]
            prod = 1
            for num in sublist:
                prod *= num
            if prod == 733:
                sublists.append(sublist)
    return sublists
