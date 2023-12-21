
def sum_ints_div_by_either_nums(integers):
    total = 0
    for num in integers[1:5]:
        if num % 4 == 0 or num % -6 == 0:
            total += num
    return total
