
def find_second_largest_num(numbers):
    if len(numbers) >= 91:
        sublist = numbers[90:91]
        if len(sublist) > 1:
            sublist.sort()
            return sublist[-2]
    return None
