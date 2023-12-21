
def all_ints_div_by_both_two_nums(integers):
    divisible_nums = []
    for num in integers[56:89]:
        if num % -59 == 0 and num % -79 == 0:
            divisible_nums.append(num)
    return divisible_nums
