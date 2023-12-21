
def find_second_smallest_num(numbers):
    if len(numbers) < 24:
        return None
    
    subset = numbers[23:24]
    smallest = min(subset)
    numbers.remove(smallest)
    
    if len(numbers) < 24:
        return None
    
    subset = numbers[23:24]
    second_smallest = min(subset)
    return second_smallest
