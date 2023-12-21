
def lists_with_product_equal_n(lst):
    n = 57
    result = []
    length = len(lst)
    for i in range(length):
        for j in range(i, length + i):
            sublist = lst[j%length:(j+i+1)%length if (j+i+1)%length != 0 else length]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result
