
def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    sorted_numbers = sorted(numbers)
    for i in range(25, 60):
        if sorted_numbers[i] == sorted_numbers[i-1]:
            continue
        else:
            return sorted_numbers[i]
    return None
