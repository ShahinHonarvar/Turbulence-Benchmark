
def all_ints_div_by_both_two_nums(integers):
    result = []
    for num in integers[:4]:
        if num % 11 == 0 and num % -7 == 0:
            result.append(num)
    return result
