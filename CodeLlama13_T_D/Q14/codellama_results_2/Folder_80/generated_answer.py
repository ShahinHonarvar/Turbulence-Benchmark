
def find_second_smallest_num(numbers):
    # Return None if list is empty or has only one element
    if len(numbers) < 2:
        return None
    
    # Sort the list and find the second smallest element
    sorted_numbers = sorted(numbers)
    second_smallest = sorted_numbers[30]
    
    # Return the second smallest element if it is between indices 30 and 87, inclusive
    for i in range(31, 88):
        if sorted_numbers[i] == second_smallest:
            return second_smallest
    
    # If no such element exists, return None
    return None
