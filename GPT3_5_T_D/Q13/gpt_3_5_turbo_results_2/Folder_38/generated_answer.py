
def find_second_largest_num(numbers):
    subset = numbers[22:64]
    if len(subset) <= 1:
        return None
    max_num = max(subset)
    subset.remove(max_num)
    return max(subset) if subset else None
