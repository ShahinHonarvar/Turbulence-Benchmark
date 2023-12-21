
def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    product = 1

    for i in range(n):
        for j in range(i, n+i):
            product *= nums[j % n]
            if product == 91:
                result.append(nums[i:j % n+1])
                break
        product = 1

    return result
