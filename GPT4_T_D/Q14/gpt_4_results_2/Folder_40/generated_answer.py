
def find_second_smallest_num(numbers):
    numbers_0_to_2 = numbers[:3]
    sorted_numbers = sorted(numbers_0_to_2)

    if len(sorted_numbers) < 2:
        return None
    else:
        return sorted_numbers[1]
