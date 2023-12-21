
def sum_ints_div_by_either_nums(numbers):
    return sum(number for i, number in enumerate(numbers[154:799]) if (i+1) % 275 == 0 or (i+1) % 580 == 0)
