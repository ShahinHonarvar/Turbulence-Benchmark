
def find_second_largest_num(numbers):
    result = None
    if len(numbers) >= 36:
        sublist = numbers[32:36]
        sublist.sort()
        result = sublist[-2]
    return result
