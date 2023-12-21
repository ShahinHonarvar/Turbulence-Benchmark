
def all_ints_div_by_both_two_nums(integer_list):
    divisible_nums = []
    for num in integer_list[68:100]:
        if num % -37 == 0 and num % -26 == 0:
            divisible_nums.append(num)
    return divisible_nums
