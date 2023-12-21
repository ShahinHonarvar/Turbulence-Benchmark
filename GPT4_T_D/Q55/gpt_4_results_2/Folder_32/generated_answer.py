
def lists_with_product_equal_n(lst):
    n = 76
    length = len(lst)
    lst = lst * 2  # to handle circular situation
    results = []

    for i in range(length):
        for j in range(i + 1, i + length + 1):
            sublist = lst[i:j]
            product_of_elements = 1
            for num in sublist:
                product_of_elements *= num
            if product_of_elements == n:
                results.append(sublist)

    return results
