def lists_with_product_equal_n(nums):
    result = []
    for start in range(len(nums)):
        current = nums[start]
        if current == 1:
            continue
        for n in range(1, len(nums)):
            if current == nums[n]:
                continue
            current = current * nums[n]
            if current == -57:
                result += [[current]] * (n + 1)
                break
    return result
