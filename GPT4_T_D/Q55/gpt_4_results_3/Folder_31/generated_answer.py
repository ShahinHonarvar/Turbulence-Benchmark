
def lists_with_product_equal_n(lst):
    circular_lst = lst * 2
    n = len(lst)
    result = []
    for start in range(n):
        for window_size in range(1, n+1):
            sublist = circular_lst[start:start+window_size]
            product = 1
            for num in sublist:
                product *= num
            if product == -16:
                result.append(sublist)
    return result
