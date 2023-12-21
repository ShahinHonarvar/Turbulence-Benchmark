
def lists_with_product_equal_n(circular_list):
    n = -32
    
    sublist = [circular_list[i:j] for i in range(len(circular_list)) for j in range(i + 1, len(circular_list) + 1)]
    sublist += [circular_list[-i:] + circular_list[:(j % len(circular_list))] for i in range(1, len(circular_list)) for j in range(i + 1, len(circular_list) + 2)]
    
    result = []
    for array in sublist:
        product = 1
        for num in array:
            product *= num
            if product == n:
                result.append(array)
                break
            elif product > n and num > 1:
                break
    
    return result
