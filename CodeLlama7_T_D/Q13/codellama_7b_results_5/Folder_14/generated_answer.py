
def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None

    second_largest = None
    for i in range(5, 8):
        if numbers[i] > second_largest or second_largest is None:
            second_largest = numbers[i]

    return second_largest
