
def sum_ints_div_by_either_nums(lst):
    sum_numbers = 0
    for number in lst[36:86]:
        if number % -27 == 0 or number % -96 == 0:
            sum_numbers += number
    return sum_numbers
