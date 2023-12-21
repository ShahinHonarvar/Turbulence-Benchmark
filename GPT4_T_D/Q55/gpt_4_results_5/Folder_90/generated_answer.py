
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    extended_list = circular_list * 2
    result = []
    for i in range(n):
        for j in range(i+1, i+n+1):
            sub = extended_list[i:j]
            product = 1
            for num in sub:
                product *= num
            if product == -690:
                result.append(sub)
    return result
