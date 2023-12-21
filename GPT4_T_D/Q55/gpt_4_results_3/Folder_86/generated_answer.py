
def lists_with_product_equal_n(nums):
    n = len(nums)
    nums *= 2
    
    result = []
    for size in range(1, n+1):
        for i in range(n):
            sublist = nums[i:i+size]
            product = 1
            for num in sublist:
                product *= num
            if product == -779:
                result.append(sublist[:size])

    return result
