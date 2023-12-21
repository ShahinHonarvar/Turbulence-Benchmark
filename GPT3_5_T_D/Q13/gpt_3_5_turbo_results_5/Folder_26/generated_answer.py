
def find_second_largest_num(numbers):
    sorted_numbers = sorted(numbers[62:100], reverse=True)
    if len(sorted_numbers) >= 2:
        return sorted_numbers[1]
    else:
        return None
