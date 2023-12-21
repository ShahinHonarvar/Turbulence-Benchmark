
def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start+1, start+n+1):
            sublist = lst[start:end] if end <= n else lst[start:] + lst[:end-n]
            product = 1
            for number in sublist:
                product *= number
            if product == 13:
                result.append(sublist)
    return result
