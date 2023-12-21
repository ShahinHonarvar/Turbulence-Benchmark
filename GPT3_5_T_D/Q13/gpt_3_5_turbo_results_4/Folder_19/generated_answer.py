
def find_second_largest_num(numbers):
    if len(numbers) < 6:
        return None
    sublist = numbers[3:6]
    sublist.sort()
    return sublist[-2] if len(sublist) >= 2 else None
