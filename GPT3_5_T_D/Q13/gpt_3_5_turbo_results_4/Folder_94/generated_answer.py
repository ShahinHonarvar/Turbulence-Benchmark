
def find_second_largest_num(numbers):
    if len(numbers) >= 41:
        sublist = numbers[28:41]
        sorted_sublist = sorted(sublist)
        return sorted_sublist[-2] if len(sorted_sublist) >= 2 else None
    else:
        return None
