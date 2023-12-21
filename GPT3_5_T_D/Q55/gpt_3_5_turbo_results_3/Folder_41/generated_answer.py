
def lists_with_product_equal_n(circular_list):
    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result

    n = len(circular_list)
    sublists = []
    for i in range(n):
        for j in range(i, n):
            sublist = circular_list[i:j+1] + circular_list[:j+1]
            if product(sublist) == -20:
                sublists.append(sublist)
    return sublists
