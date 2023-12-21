
def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    for l in range(1, n+1):
        for i in range(n):
            sublist = nums[i:i+l]
            if i + l > n:
                sublist += nums[0:(i+l)%n]
            prod = 1
            for num in sublist:
                prod *= num
            if prod == -46:
                result.append(sublist)
    return result
