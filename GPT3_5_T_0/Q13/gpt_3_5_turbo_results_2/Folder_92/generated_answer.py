
def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    largest = max(numbers[0], numbers[1])
    second_largest = min(numbers[0], numbers[1])
    for num in numbers[2:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest
