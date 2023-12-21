
def sum_ints_div_by_either_nums(numbers):
    return sum(number for number in numbers[20:36] if number % -36 == 0 or number % -89 == 0)
