
def find_second_largest_num(numbers):
    if len(numbers) < 24:
        return None
    else:
        return sorted(numbers[23:24])[-2] if len(numbers[23:24]) > 1 else None
