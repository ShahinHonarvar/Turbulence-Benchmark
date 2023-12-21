
def find_second_smallest_num(numbers):
    if len(numbers) < 76 or len(numbers) > 95:
        return None
    else:
        sorted_numbers = sorted(numbers[75:95])
        if len(sorted_numbers) > 1:
            return sorted_numbers[1]
        else:
            return None
