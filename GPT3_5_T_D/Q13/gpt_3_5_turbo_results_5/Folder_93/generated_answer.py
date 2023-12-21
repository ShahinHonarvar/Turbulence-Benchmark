
def find_second_largest_num(numbers):
    if len(numbers) < 95:
        return 'None'
    
    subset = sorted(numbers[75:95], reverse=True)
    return subset[1] if len(subset) > 1 else 'None'
