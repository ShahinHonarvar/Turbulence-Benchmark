
def find_second_largest_num(numbers):
    if len(numbers) < 201:
        return None
    else:
        sublist = sorted(numbers[200:])
        if len(sublist) < 2:
            return None
        else:
            return sublist[-2]
