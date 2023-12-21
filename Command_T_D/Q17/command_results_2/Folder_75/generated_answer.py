
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(20, 93):
        if i % -92 == 0 and i % -50 == 0:
            result.append(i)
    return result
