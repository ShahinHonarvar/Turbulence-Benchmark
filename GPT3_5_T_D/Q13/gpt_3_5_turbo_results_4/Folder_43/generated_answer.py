
def find_second_largest_num(numbers):
    if len(numbers) < 87:
        return None
    sublist = numbers[68:87]
    sublist.sort()
    if len(set(sublist)) < 2:
        return None
    return sublist[-2]
