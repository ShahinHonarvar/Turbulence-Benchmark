
def lists_with_product_equal_n(circular_list):
    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result

    sublists = []
    size = len(circular_list)
    for i in range(size):
        for j in range(i + 1, size + 1):
            sublist = circular_list[i:j]
            if product(sublist) == -83:
                sublists.append(sublist)

    return sublists
