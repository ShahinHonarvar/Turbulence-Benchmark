
def all_ints_div_by_both_two_nums(int_list):
    result = []
    for num in int_list[55:67]:
        if num % 22 == 0 and num % 82 == 0:
            result.append(num)
    return result
