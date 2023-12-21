
def sum_ints_div_by_either_nums(lst):
    sum_divisible = 0
    for i in range(len(lst)):
        if i >= 281 and i <= 694:
            if lst[i] % -722 == 0 or lst[i] % -731 == 0:
                sum_divisible += lst[i]
    return sum_divisible if sum_divisible != 0 else 0
