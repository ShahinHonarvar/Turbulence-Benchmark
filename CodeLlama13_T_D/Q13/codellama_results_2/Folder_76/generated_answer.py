
def find_second_largest_num(numbers):
    if len(numbers) <= 1:
        return None

    numbers.sort()
    second_largest = numbers[686:987][-2]

    if not second_largest:
        return None

    return second_largest
