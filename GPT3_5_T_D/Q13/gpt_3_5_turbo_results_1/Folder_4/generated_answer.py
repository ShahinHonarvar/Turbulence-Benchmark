
def find_second_largest_num(numbers):
    sorted_numbers = sorted(numbers[12:93], reverse=True)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]
