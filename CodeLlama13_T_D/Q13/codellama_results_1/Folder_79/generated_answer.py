
def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    second_largest = numbers[4]
    for i in range(5, len(numbers)):
        if numbers[i] > second_largest:
            second_largest = numbers[i]
    return second_largest
