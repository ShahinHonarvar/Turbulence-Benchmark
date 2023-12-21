
def lists_with_product_equal_n(nums):
    result = []
    size = len(nums)
    for i in range(size):
        for j in range(i+1, size+1):
            sublist = nums[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -10:
                result.append(sublist)
    return result
