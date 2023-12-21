
def find_second_largest_num(numbers):
    if len(numbers) < 51:
        return None
    else:
        sublist = numbers[43:52]
        sublist.sort()
        return sublist[-2]
