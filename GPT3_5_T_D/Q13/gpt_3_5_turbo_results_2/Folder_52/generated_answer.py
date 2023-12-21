
def find_second_largest_num(numbers):
    if len(numbers) < 39:
        return None

    sublist = numbers[28:39]
    sublist.sort(reverse=True)

    return sublist[1] if len(sublist) > 1 else None
