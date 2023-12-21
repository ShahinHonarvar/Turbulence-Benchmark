
def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    numbers = sorted(numbers)
    second_largest = numbers[4]
    for i in range(1, 5):
        if numbers[i] == second_largest:
            return None
    return second_largest
