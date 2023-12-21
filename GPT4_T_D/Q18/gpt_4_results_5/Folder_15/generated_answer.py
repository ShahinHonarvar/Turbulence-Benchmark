
def sum_ints_div_by_either_nums(lst):
    sum_numbers = 0
    for num in lst[:3]:
        if num % -2 == 0 or num % 3 == 0:
            sum_numbers += num
    return sum_numbers
