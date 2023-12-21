
def find_second_smallest_num(numbers):
    if 66 <= len(numbers)-1 <= 93:
        sorted_numbers = sorted(numbers[66:94])
        if len(sorted_numbers) > 1:
            return sorted_numbers[1]
    return None
