
def find_second_largest_num(numbers):
    numbers_sublist = numbers[14:65]
    if len(numbers_sublist)<2:
        return None
    else:
        numbers_sublist.sort()
        return numbers_sublist[-2]
