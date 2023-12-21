
def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    sorted_numbers = sorted(numbers)
    second_largest = sorted_numbers[4]
    for i in range(1, 5):
        if sorted_numbers[i] != second_largest:
            return second_largest
    return None
