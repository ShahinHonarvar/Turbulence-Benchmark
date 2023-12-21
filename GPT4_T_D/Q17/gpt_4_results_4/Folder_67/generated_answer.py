
def all_ints_div_by_both_two_nums(num_list):
    result = []
    for num in num_list[24:33]:
        if num % 35 == 0 and num % 87 == 0:
            result.append(num)
    return result
