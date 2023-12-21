
def find_second_largest_num(numbers):
    if len(numbers) < 60:
        return None
    sublist = numbers[25:60]
    sublist.sort()
    return sublist[-2] if len(sublist) > 1 else None
