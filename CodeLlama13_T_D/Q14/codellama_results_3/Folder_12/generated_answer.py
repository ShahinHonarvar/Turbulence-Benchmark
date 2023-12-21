
def find_second_smallest_num(numbers):
    # Get a list of numbers from index 31 to index 72, both inclusive
    relevant_numbers = numbers[30:73]
    
    # Find the second smallest element in the list
    second_smallest = sorted(relevant_numbers)[1]
    
    # Return the second smallest element if it exists, otherwise return None
    return second_smallest if len(second_smallest) > 0 else None
