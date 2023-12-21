
def all_ints_not_div_by_num(numbers):
    return [num for i, num in enumerate(numbers[1:7]) if num % 7 != 0]
