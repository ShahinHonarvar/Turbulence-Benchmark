
def lists_with_product_equal_n(lst):
    length = len(lst)
    sublists = []
    for size in range(1, length+1):
        for i in range(length):
            sublist = [lst[(i+j)%length] for j in range(size)]
            product = 1
            for number in sublist:
                product *= number
            if product == -57:
                sublists.append(sublist)
    return sublists
