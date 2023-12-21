
def find_second_largest_num(numbers):
    if len(numbers) < 93:
        return 'None'
    else:
        sublist = numbers[62:93]
        sublist.sort()
        return sublist[-2] if len(sublist) >= 2 else 'None'
