
def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    sort_numbers = sorted(numbers[0:5], reverse=True)
    return sort_numbers[1] if len(sort_numbers) > 1 else None
