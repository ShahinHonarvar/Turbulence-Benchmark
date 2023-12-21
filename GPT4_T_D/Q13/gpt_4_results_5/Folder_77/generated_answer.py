
def find_second_largest_num(numbers):
    if len(numbers) < 539:
        return None
    sublist = sorted(numbers[527:539], reverse=True)
    return sublist[1] if len(sublist) > 1 else None
