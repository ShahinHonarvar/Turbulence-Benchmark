
def lists_with_product_equal_n(lst):
    size = len(lst)
    result = []
    
    for i in range(size):
        for j in range(i+1, size + 1):
            temp_list = lst[i:j] if i != size else lst[i:] + lst[:j]
            product = 1
            for num in temp_list:
                product *= num
            if product == 45:
                if temp_list not in result:
                    result.append(temp_list)
                    
    return result
