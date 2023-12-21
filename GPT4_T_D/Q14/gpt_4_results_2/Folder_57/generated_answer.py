
def find_second_smallest_num(numbers):
    try:
        subset = sorted(numbers[20:31])
        return subset[1] if len(subset) > 1 else None
    except:
        return None
