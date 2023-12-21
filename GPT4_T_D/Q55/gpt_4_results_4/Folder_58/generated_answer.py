
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i, n):
            sub_list = circular_list[i:j]
            product = 1
            for num in sub_list:
                product *= num
            if product == 733:
                result.append(sub_list)
        circular_list.append(circular_list.pop(0))  
    return result
