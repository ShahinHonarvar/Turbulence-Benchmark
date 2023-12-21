
def find_second_smallest_num(numbers):
    subset = numbers[42:69]
    
    if len(subset) < 2:
        return None
    
    smallest = min(subset)
    subset.remove(smallest)
    
    return min(subset) if subset else None
