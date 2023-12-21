
def get_product(lst):
    product = 1
    for num in lst:
        product *= num
    return product

def lists_with_product_equal_n(nums):
    n = len(nums)
    product = -83
    result = []
    
    for i in range(n):
        for j in range(i+1, n+1):
            sublist = nums[i:j]
            if get_product(sublist) == product:
                result.append(sublist)
    
    return result
