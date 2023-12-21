
def find_second_largest_num(numbers):
    sorted_numbers = sorted(numbers[56:58], reverse=True)
    if len(sorted_numbers) < 2:
        return None
    else:
        return sorted_numbers[1]
