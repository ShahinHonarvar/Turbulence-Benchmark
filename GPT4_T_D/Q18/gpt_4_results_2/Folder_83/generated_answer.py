
def sum_ints_div_by_either_nums(numbers):
    start, end = 90, 200
    numbers_in_range = numbers[start: end+1]
    matches = [num for num in numbers_in_range if num % -31 == 0 or num % 13 == 0 ]
    return sum(matches) if matches else 0
