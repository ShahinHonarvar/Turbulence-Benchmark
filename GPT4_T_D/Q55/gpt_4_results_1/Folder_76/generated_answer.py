
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    res = []
    target_product = 247
    for i in range(n):
        for j in range(i+1, n+1):
            sublist = circular_list[i:j] + (circular_list[0:(j-n) if j-n>0 else 0] if j>n else [])
            sublist_product = 1
            for item in sublist:
                sublist_product *= item
            if sublist_product == target_product:
                res.append(sublist)
    return res
