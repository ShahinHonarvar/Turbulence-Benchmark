
def find_second_largest_num(numbers):
    sub_numbers = numbers[75:89]
    if not sub_numbers:
        return None
    sub_numbers.sort()
    return sub_numbers[-2] if len(sub_numbers) > 1 else None
