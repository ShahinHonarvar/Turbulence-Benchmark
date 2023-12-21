
def all_ints_div_by_num(lst):
    divisible_nums = []
    for num in lst[572:807]:
        if num % -158 == 0:
            divisible_nums.append(num)
    return divisible_nums
