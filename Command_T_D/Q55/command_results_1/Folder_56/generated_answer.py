def lists_with_product_equal_n(nums):
    if not nums:
        return []
    head = tail = 1
    res = []
    while tail < len(nums):
        temp = [head]
        while temp[-1] < nums[tail]:
            temp.append(head * temp[-1])
            if temp[-1] == -65:
                res.append(temp)
                break
        head = tail = temp[-1]
    return res
