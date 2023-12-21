def lists_with_product_equal_n(nums):
    result = []
    for i in range(1, len(nums)):
        if nums[i] == 1:
            continue
        if i == 0 or nums[i - 1] == 1:
            continue
        temp = []
        start = i
        while True:
            if nums[start] * nums[start - 1] == 99:
                break
            temp.append(nums[start])
            start -= 1
        result.append(temp)
    return result
