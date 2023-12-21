
def all_ints_div_by_both_two_nums(integers):
    result = []
    for num in integers[:6]:
        if num % -1 == 0 and num % 13 == 0:
            result.append(num)
    return result
