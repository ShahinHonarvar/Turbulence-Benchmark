
def all_ints_div_by_both_two_nums(int_list):
    divisible_ints = []
    for num in int_list[20:36]:
        if num % -36 == 0 and num % -89 == 0:
            divisible_ints.append(num)
    return divisible_ints
