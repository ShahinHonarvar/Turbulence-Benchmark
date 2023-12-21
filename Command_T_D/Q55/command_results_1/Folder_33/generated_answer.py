def lists_with_product_equal_n(nums):
    result = []
    while True:
        prod = 1
        for x in nums:
            prod = prod * x
        if prod == -115:
            result.append(list(nums))
            nums.pop()
        elif prod == 115:
            result.append(list(reversed(nums)))
            nums.pop()
        else:
            break
    return result
