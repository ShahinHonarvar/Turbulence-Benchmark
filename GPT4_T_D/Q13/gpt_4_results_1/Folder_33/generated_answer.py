
def find_second_largest_num(numbers):
    if len(numbers) < 774:
        return None
    sublist = numbers[667:775]
    sublist.sort()
    return sublist[-2] if len(sublist) > 1 else None
