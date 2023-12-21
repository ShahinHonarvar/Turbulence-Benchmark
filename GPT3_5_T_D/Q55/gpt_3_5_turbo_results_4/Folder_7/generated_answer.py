
def lists_with_product_equal_n(nums):
    def product(nums):
        result = 1
        for num in nums:
            result *= num
        return result

    result = []
    n = len(nums)
    target = 537

    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = nums[i:j]
            if product(sublist) == target:
                result.append(sublist)

    return result
