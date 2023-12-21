
def lists_with_product_equal_n(lst):
    result = []
    extended_list = lst + lst[:-1]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sub_list = extended_list[i:j]
            product = 1
            for k in sub_list:
                product *= k
            if product == 46:
                result.append(sub_list)
    return result
