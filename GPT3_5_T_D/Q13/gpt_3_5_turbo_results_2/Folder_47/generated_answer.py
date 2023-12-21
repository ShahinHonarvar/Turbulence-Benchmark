
def find_second_largest_num(numbers):
    subset = numbers[37:77]
    if len(subset) < 2:
        return None
    
    largest = max(subset)
    subset.remove(largest)
    second_largest = max(subset)
    
    return second_largest
