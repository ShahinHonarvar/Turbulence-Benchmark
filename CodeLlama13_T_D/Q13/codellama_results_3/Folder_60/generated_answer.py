
def find_second_largest_num(numbers):
    if len(numbers) < 85:
        return None
    second_largest = sorted(numbers)[74]
    for i in range(75, 86):
        if numbers[i] > second_largest:
            second_largest = numbers[i]
    return second_largest
