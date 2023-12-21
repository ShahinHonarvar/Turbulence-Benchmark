
def all_ints_div_by_both_two_nums(numbers):
    return [x for x in numbers[1:8+1] if x % -9 == 0 and x % -3 == 0]
