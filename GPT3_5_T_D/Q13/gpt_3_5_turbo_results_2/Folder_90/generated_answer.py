
def find_second_largest_num(numbers):
    if len(numbers) < 747:
        return None
    sublist = numbers[262:747]
    sorted_sublist = sorted(sublist)
    return sorted_sublist[-2]
