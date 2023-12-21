
def find_second_smallest_num(numbers):
    # Sort the numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Check if there are at least 50 elements in the list
    if len(sorted_numbers) >= 50:
        # Get the second smallest element from index 22 to index 50
        second_smallest = sorted_numbers[22:51][1]
        return second_smallest
    else:
        return None
