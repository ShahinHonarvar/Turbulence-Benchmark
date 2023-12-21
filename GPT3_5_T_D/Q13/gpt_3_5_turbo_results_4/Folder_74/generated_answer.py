
def find_second_largest_num(numbers):
    if len(numbers) < 79:
        return None
    
    subset = sorted(numbers[17:79], reverse=True)
    return subset[1] if len(subset) >= 2 else None
