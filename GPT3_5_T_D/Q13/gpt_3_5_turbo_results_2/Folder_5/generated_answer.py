
def find_second_largest_num(numbers):
    if len(numbers) < 10:
        return None
    else:
        subset = sorted(numbers[8:10], reverse=True)
        return subset[1] if len(subset) > 1 else None
