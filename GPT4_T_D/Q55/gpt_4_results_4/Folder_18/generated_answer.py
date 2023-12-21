
def lists_with_product_equal_n(nums):
    result = []
    if not nums: return result
    
    length = len(nums)
    nums.extend(nums)
    
    for i in range(length):
        for j in range(i+1, i+length+1):
            sublist = nums[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 36:
                result.append(sublist)
    
    return result
