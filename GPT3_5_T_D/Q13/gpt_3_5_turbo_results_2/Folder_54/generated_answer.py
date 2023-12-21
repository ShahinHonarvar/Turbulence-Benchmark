
def find_second_largest_num(numbers):
    if len(numbers) >= 56:
        sublist = numbers[34:56]
        sublist.sort(reverse=True)
        return sublist[1] if len(sublist) >= 2 else None
    else:
        return None
