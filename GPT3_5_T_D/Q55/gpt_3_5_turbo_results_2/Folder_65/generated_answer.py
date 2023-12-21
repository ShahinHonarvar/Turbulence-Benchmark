
def lists_with_product_equal_n(nums):
    result = []

    for i in range(len(nums)):
        prod = 1

        for j in range(i, len(nums) + i):
            prod *= nums[j % len(nums)]

            if prod == 46:
                result.append(nums[i: j % len(nums) + 1])

    return result
