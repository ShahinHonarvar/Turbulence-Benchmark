
def find_second_largest_num(numbers):
    if len(numbers) >= 24:
        sublist = numbers[23:24]
        sorted_sublist = sorted(sublist, reverse=True)
        if len(sorted_sublist) > 1:
            return sorted_sublist[1]
    return None
