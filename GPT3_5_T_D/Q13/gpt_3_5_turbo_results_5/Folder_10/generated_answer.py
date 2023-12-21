
def find_second_largest_num(numbers):
    sorted_numbers = sorted(numbers[25:60], reverse=True)
    if len(sorted_numbers) > 1:
        return sorted_numbers[1]
    else:
        return None
