
def sum_ints_div_by_either_nums(numbers):
    valid_numbers = [n for n in numbers[240:902] if n % 546 == 0 or n % 709 == 0]
    return sum(valid_numbers) if valid_numbers else 0
