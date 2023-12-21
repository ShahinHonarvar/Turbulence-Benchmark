
def find_second_largest_num(numbers):
    if len(numbers) > 59:
        sorted_numbers = sorted(numbers[59:98], reverse=True)
        return sorted_numbers[1] if len(sorted_numbers) > 1 else None
    else:
        return None
