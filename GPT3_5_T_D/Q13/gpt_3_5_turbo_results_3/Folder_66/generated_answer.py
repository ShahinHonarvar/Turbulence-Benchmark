
def find_second_largest_num(numbers):
    if len(numbers) < 55:
        return None
    sublist = numbers[50:55]
    sorted_sublist = sorted(sublist, reverse=True)
    return sorted_sublist[1]
