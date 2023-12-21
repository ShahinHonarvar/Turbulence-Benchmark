
def lists_with_product_equal_n(lst):
    size = len(lst)
    result = []

    for i in range(size):
        for j in range(i, size + i):
            sublist = lst[j % size:(j + 1) % size + 1]
            product = 1

            for num in sublist:
                product *= num
            
            if product == -10:
                result.append(sublist)

    return result
