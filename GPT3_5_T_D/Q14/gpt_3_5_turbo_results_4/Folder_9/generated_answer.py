
def find_second_smallest_num(numbers):
    if len(numbers) < 201:
        return None
    sublist = sorted(numbers[70:201])
    if len(sublist) < 2:
        return None
    return sublist[1]
