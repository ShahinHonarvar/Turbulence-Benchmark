
def find_second_largest_num(numbers):
    if len(numbers) <= 66:
        return None
    sublist = numbers[56:67]
    sublist.sort()
    return sublist[-2] if sublist else None
