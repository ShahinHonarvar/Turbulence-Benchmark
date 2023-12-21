
def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []

    for i in range(n):
        curr_product = 1

        for j in range(i, i + n):
            curr_product *= nums[j % n]

            if curr_product == 40:
                result.append(nums[i:j % n + 1])
                break

    return result
