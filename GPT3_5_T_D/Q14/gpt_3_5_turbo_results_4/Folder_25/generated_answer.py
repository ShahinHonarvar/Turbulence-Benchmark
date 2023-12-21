
def find_second_smallest_num(numbers):
    if len(numbers) < 77:
        return None
    sublist = sorted(numbers[37:77])
    if len(sublist) < 2:
        return None
    return sublist[1]
