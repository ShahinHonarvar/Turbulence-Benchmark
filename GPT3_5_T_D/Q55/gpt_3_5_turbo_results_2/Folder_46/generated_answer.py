
def lists_with_product_equal_n(lst):
    def product(sub_list):
        result = 1
        for num in sub_list:
            result *= num
        return result
    
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sub = lst[i:j+1] + lst[:j-i]
            if product(sub) == 53:
                result.append(sub)
    
    return result
