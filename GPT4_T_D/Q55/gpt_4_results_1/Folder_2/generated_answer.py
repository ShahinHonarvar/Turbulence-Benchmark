
def lists_with_product_equal_n(lst):
    n = -968
    list_len = len(lst)
    result = []

    for start in range(list_len):
        for end in range(start+1, start + list_len + 1):
            sublist = lst[start:end] if end <= list_len else lst[start:] + lst[:end-list_len]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
            
    return result
