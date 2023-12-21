
def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None

    sorted_numbers = sorted(numbers)
    second_smallest = sorted_numbers[19:93]

    if not second_smallest:
        return None

    return second_smallest[0]
