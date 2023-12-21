
def product(nums):
    res = 1
    for num in nums:
        res *= num
    return res

def lists_with_product_equal_n(nums):
    n = len(nums)
    target = 57
    result = []
    for start in range(n):
        for end in range(start, start+n):
            subset = nums[start:end+1] if start <= end else nums[start:] + nums[:end+1]
            if product(subset) == target:
                result.append(subset)
    return result
