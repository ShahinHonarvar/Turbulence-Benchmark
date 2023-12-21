
def find_second_largest_num(numbers):
    sublist = numbers[19:93] # Note: index 93 is not inclusive
    sorted_sublist = sorted(sublist, reverse=True)
    return sorted_sublist[1] if len(sorted_sublist) > 1 else None
