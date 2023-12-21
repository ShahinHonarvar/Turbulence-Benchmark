
def lists_with_product_equal_n(nums):
    result = []
    length = len(nums)
    
    for i in range(length):
        for j in range(i+1, length+1):
            sub_list = nums[i:j]
            product = 1
            for num in sub_list:
                product *= num
            if product == -91:
                result.append(sub_list)
    
    return result
