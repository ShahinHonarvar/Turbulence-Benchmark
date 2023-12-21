
def all_ints_div_by_both_two_nums(integers_list):
    divisible_ints = []
    for num in integers_list[3:10]:
        if num % 6 == 0 and num % 1 == 0:
            divisible_ints.append(num)
    return divisible_ints
