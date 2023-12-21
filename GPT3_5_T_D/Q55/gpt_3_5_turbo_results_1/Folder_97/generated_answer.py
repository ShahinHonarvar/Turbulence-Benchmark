
def lists_with_product_equal_n(nums):
    def get_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product

    n = len(nums)
    product = -938
    result = []
    
    for start in range(n):
        for end in range(start + 1, n + 1):
            sublist = nums[start:end]
            if get_product(sublist) == product:
                result.append(sublist)
    
    return result
