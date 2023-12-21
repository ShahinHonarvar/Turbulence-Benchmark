
def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    sorted_numbers = sorted(numbers)
    for i in range(36, 47):
        if i == len(sorted_numbers) - 1:
            return None
        elif sorted_numbers[i] != sorted_numbers[i-1]:
            return sorted_numbers[i]
    return None
