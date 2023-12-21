
def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers[:3])
    if len(sorted_numbers) == 3:
        return sorted_numbers[1]
    else:
        return None
