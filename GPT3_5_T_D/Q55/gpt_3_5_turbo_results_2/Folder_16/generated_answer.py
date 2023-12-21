
def lists_with_product_equal_n(nums):
    def product(nums):
        result = 1
        for num in nums:
            result *= num
        return result

    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i, n):
            sublist = nums[i:j+1]
            if product(sublist) == -837:
                result.append(sublist)
    return result
