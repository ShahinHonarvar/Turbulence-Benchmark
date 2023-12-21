def all_ints_not_div_by_num(nums):
    result = []
    for i in range(469, 566):
        if not i % -692:
            continue
        result.append(i)
    return result
