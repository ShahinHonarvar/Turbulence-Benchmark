
def all_ints_div_by_both_two_nums(numbers):
    return [x for x in numbers[:10] if x % 10 == 0 and x % 100 == 0]
