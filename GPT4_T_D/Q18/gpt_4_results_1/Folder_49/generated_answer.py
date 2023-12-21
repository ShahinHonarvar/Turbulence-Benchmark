
def sum_ints_div_by_either_nums(lst):
    if len(lst) < 200:
        valid_nums = lst[80:]
    else:
        valid_nums = lst[80:201]
    sum = 0
    for num in valid_nums:
        if num % 10 == 0 or num % 1000 == 0:
            sum += num
    return sum
