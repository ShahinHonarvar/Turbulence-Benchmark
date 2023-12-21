
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    
    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    
    for start in range(n):
        for end in range(start, n):
            sub_list = circular_list[start:end+1] + circular_list[0:start]
            if product(sub_list) == 49:
                result.append(sub_list)
    
    return result
