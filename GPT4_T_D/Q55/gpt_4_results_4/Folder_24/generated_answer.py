
def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    if size == 0: return result

    for start in range(size):
        for sublist_size in range(1, size + 1):
            sublist = [lst[(start + i) % size] for i in range(sublist_size)]
            product = 1
            for num in sublist:
                product *= num
            if product == -89:
                result.append(sublist)
    return result
