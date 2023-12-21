
def find_second_largest_num(numbers):
    if len(numbers) < 3:
        return None
    sorted_numbers = sorted(numbers[:3])
    return sorted_numbers[-2]
