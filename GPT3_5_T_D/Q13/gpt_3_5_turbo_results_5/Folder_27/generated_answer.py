
def find_second_largest_num(numbers):
    if len(numbers) < 67:
        return None
    sublist = numbers[66:94]
    if len(set(sublist)) < 2:
        return None
    return sorted(set(sublist))[-2]
