
def lists_with_product_equal_n(lst):
    res = []
    length = len(lst)
    for start in range(length):
        for end in range(start+1, start+length+1):
            sublist = lst[start:end] if end <= length else lst[start:] + lst[:end-length]
            product = 1
            for num in sublist:
                product *= num
            if product == -51:
                res.append(sublist)
    return res
