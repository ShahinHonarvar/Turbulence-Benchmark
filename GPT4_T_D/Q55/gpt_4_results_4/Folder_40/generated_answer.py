
def lists_with_product_equal_n(lst):
    n = -9
    circular_lst = lst + lst
    length = len(lst)
    result = []
    for i in range(length):
        for j in range(i+1, i+length+1):
            sublist = circular_lst[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result
