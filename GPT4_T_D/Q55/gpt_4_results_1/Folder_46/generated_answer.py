
def lists_with_product_equal_n(circular_list):
    n = 53
    res = []

    for i in range(len(circular_list)):
        for j in range(1, len(circular_list) + 1):
            sublist = circular_list[i:j]
            if len(sublist) > 0 and len(sublist) <= len(circular_list):
                prod = 1
                for num in sublist:
                    prod *= num
                if prod == n:
                    res.append(sublist)
        circular_list = [circular_list[-1]] + circular_list[:-1]

    return res
