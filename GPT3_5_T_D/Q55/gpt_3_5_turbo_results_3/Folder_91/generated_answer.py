
def lists_with_product_equal_n(lst):
    result = []
    
    def product(nums):
        prod = 1
        for num in nums:
            prod *= num
        return prod
    
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            sub_list = lst[i:j]
            if product(sub_list) == 2:
                result.append(sub_list)
    
    return result
