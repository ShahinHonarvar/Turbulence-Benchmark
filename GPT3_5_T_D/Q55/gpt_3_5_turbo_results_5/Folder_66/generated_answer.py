
def lists_with_product_equal_n(circular_list):
    def product_list(lst):
        result = 1
        for num in lst:
            result *= num
        return result

    result = []
    size = len(circular_list)
    for i in range(size):
        for j in range(i + 1, size + i):
            sublist = circular_list[i:j]
            if product_list(sublist) == 78:
                result.append(sublist)
    return result
