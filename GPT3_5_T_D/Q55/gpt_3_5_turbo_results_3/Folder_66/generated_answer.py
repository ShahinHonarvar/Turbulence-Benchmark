
def lists_with_product_equal_n(numbers):
    product = 78
    sublists = []
    length = len(numbers)
    for i in range(length):
        sublist = []
        sublist_product = 1
        for j in range(i, length + i):
            sublist.append(numbers[j % length])
            sublist_product *= numbers[j % length]
            if sublist_product == product:
                sublists.append(sublist.copy())
    return sublists
