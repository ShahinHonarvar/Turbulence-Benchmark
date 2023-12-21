def all_ints_div_by_num(nums):
    result = []
    for i in range(255, 618):
        if i % 965 == 0:
            result.append(i)
    return result
