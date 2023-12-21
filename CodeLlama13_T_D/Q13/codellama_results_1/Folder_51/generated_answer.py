
def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    second_largest = numbers[1]
    for i in range(2, 9):
        if numbers[i] > second_largest:
            second_largest = numbers[i]
    return second_largest
