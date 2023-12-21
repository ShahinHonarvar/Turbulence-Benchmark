
def all_ints_div_by_num(lst):
    divisible_nums = []
    for num in lst[62:71]:
        if num % 58 == 0:
            divisible_nums.append(num)
    return divisible_nums
