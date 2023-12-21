
def all_ints_div_by_both_two_nums(num_list):
    result = []
    for num in num_list[281:695]:
        if num % -722 == 0 and num % -731 == 0:
            result.append(num)
    return result
