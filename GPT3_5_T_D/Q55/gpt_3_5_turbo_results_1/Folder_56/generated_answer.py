
def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    product = 1

    for i in range(n):
        for j in range(i, i+n):
            product *= nums[j % n]
            if product == -65:
                sublist = nums[i:j % n + 1]
                result.append(sublist)
            if product == 0:
                break
        product = 1

    return result
