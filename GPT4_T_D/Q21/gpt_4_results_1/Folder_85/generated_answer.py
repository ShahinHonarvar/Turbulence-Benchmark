
def all_ints_div_by_num(lst):
    divisible_ints = []
    for num in lst[6:9]:
        if num % -9 == 0:
            divisible_ints.append(num)
    return divisible_ints
