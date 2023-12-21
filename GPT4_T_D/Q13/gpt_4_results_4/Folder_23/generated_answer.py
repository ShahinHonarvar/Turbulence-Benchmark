
def find_second_largest_num(numbers):
    if len(numbers) >= 72:
        sublist = numbers[52:72]
        sublist.sort()
        return sublist[-2]
    return None
