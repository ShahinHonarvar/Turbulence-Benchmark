
def find_second_largest_num(numbers):
    if len(numbers) < 94:
        return None
    sublist = numbers[29:94]
    sublist.sort(reverse=True)
    return sublist[1]
