
def find_second_largest_num(numbers):
    numbers = numbers[12:93]
    if len(numbers) < 2:
        return None
    largest = numbers[0]
    second_largest = float('-inf')
    for num in numbers[1:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest
