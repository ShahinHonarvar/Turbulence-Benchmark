
def find_second_largest_num(numbers):
    if len(numbers) < 87:
        return None
    sublist = numbers[82:87]
    sublist.sort()
    return sublist[-2] if len(sublist) >= 2 else None
