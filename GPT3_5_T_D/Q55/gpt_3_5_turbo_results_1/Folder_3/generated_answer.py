
def lists_with_product_equal_n(nums):
    result = []
    if len(nums) == 0:
        return result

    def check_product(sub_nums, n):
        product = 1
        for num in sub_nums:
            product *= num
        return product == n

    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            if check_product(nums[i:j], -22):
                result.append(nums[i:j])

    return result
