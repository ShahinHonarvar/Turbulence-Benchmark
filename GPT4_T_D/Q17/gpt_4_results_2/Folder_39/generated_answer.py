
def all_ints_div_by_both_two_nums(num_list):
    divisible_by_both = []
    for index in range(13, 77):
        try:
            if num_list[index] % (-66) == 0 and num_list[index] % (-32) == 0:
                divisible_by_both.append(num_list[index])
        except IndexError:
            break
    return divisible_by_both
