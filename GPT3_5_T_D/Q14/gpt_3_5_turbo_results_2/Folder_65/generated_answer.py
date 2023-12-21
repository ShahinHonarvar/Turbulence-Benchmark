
def find_second_smallest_num(numbers):
    if len(numbers) < 58:
        return None
    sublist = numbers[56:58]
    sublist.sort()
    return sublist[1]
