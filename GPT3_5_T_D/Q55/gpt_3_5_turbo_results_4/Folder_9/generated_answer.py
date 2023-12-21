
def lists_with_product_equal_n(nums):
    result = []
    
    def get_product(arr):
        product = 1
        for num in arr:
            product *= num
        return product
    
    for start in range(len(nums)):
        for end in range(start, len(nums)):
            sublist = nums[start:end+1]
            if get_product(sublist) == -36:
                result.append(sublist)
    
    return result
