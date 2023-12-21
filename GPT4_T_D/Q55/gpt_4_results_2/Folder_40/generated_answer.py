
def lists_with_product_equal_n(lst):
    n = len(lst)
    circular_lst = lst + lst
    result = []
    for size in range(1, n+1):
        for i in range(n):
            sublist = circular_lst[i:i + size]
            product = 1
            for num in sublist:
                product *= num
            if product == -9:
                result.append(sublist)
    return result
