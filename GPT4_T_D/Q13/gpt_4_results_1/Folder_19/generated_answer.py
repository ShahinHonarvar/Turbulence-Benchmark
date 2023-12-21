
def find_second_largest_num(numbers):
    if len(numbers) >= 6:
        sublist = numbers[3:6]
        sublist.sort()
        return sublist[-2]
    return None
