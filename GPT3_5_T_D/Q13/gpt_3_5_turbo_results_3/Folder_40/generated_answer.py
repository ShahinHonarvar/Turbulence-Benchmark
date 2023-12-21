
def find_second_largest_num(numbers):
    sorted_numbers = sorted(numbers[:3])
    if len(numbers) < 2:
        return None
    return sorted_numbers[-2]
