def lists_with_product_equal_n(nums):
    lst = [nums[0]]
    for x in nums[1:]:
        if x == -1:
            break
        if x == 0:
            lst.append([x])
            continue
        lst.append([x] + [0] * (len(lst) - 1))
    return lst
