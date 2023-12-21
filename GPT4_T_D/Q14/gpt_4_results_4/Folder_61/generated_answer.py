
def find_second_smallest_num(numbers):
    if len(numbers) < 8:
        return None
    else:
        sorted_numbers = sorted(numbers[:8])
        if len(sorted_numbers) > 1:
            return sorted_numbers[1]
        else:
            return None
