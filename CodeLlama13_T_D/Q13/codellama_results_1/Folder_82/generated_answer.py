
def find_second_largest_num(numbers):
    # Find the largest element in the list
    largest = max(numbers)
    
    # Create a new list with all elements except the largest one
    without_largest = [x for x in numbers if x != largest]
    
    # Return the second largest element from index 20 to index 200, both inclusive
    return sorted(without_largest)[19:201]
