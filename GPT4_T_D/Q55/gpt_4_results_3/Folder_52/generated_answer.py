
def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)

    def get_product(lst):
        product = 1
        for num in lst:
            product *= num
        return product

    for i in range(n):
        for j in range(1, n+1):
            sublist = circular_list[i:j] if j > i else circular_list[i:]+circular_list[:j]
            if get_product(sublist) == 37:
                result.append(sublist)
                
    return result
