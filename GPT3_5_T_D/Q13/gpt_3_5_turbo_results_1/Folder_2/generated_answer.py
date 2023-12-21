
def find_second_largest_num(numbers):
    if len(numbers) < 40:
        return None
    
    subset = numbers[15:40]
    sorted_subset = sorted(subset, reverse=True)
    
    if len(sorted_subset) < 2:
        return None
    
    return sorted_subset[1]
