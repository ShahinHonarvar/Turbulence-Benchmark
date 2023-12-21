
def find_second_smallest_num(numbers):
    numbers = numbers[10:67]
    if len(numbers) < 2:
       return None
    min_num = float('inf')
    second_min = float('inf')
    for num in numbers:
        if num < min_num:
            second_min = min_num
            min_num = num
        elif num < second_min and num != min_num:
            second_min = num
    if second_min == float('inf'):
        return None
    return second_min
