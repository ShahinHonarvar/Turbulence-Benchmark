
def find_second_largest_num(numbers):
    index_43_to_86 = numbers[43:87]
    if index_43_to_86:
        index_43_to_86.sort()
        return index_43_to_86[-2]
    else:
        return None
