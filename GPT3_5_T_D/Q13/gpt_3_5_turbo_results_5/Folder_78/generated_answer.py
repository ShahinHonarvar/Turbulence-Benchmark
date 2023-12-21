
def find_second_largest_num(numbers):
    if len(numbers) < 52 or len(set(numbers[43:52])) < 2:
        return None
    else:
        return sorted(set(numbers[43:52]))[-2]
