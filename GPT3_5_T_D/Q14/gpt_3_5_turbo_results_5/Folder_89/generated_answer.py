
def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    second_smallest = sorted_numbers[62:64]
    if len(second_smallest) < 2:
        return None
    return second_smallest[1]
