
def find_second_largest_num(numbers):
    numbers = numbers[52:72]
    if len(numbers) < 2:
        return None
    max_num = numbers[0]
    second_max_num = float('-inf')
    for num in numbers:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num < max_num:
            second_max_num = num
    return second_max_num
