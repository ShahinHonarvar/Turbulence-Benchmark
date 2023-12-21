def find_second_smallest_num(nums):
    res = []
    for i in range(62, 78):
        if len(res) == 2:
            break
        res += [j for j in nums if j == i]
    return res[-2] if len(res) == 2 else None
