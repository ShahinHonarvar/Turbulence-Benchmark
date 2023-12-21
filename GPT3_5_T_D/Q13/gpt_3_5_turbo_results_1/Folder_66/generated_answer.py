
def find_second_largest_num(numbers):
    if len(numbers) < 55:
        return None
    sublist = sorted(numbers[50:55])
    return sublist[-2] if len(sublist) >= 2 else None
