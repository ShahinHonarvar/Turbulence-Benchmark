
def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first_largest = max(numbers)
    second_largest = float('-inf')
    for num in numbers:
        if num != first_largest and num > second_largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    return second_largest
