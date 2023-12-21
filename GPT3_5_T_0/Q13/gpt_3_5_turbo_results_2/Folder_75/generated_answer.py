
def find_second_largest_num(numbers):
    if len(numbers) < 58:
        return None
    sublist = numbers[56:58]
    sublist.sort()
    return sublist[-2] if sublist[-2] != sublist[-1] else None
