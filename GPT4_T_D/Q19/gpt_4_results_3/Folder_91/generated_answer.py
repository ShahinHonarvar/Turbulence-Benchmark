
def all_ints_not_div_by_num(numbers):
    return [num for i, num in enumerate(numbers) if i > 0 and i < 5 and num % 8 != 0]
