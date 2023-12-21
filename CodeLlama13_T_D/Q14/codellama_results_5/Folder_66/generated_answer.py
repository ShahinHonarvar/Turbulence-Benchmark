
def find_second_smallest_num(numbers):
    # Check if there are at least 10 elements in the list
    if len(numbers) < 10:
        return None
    
    # Find the smallest element in the list
    smallest = min(numbers)
    
    # Filter the list to keep only the elements that are greater than the smallest element
    filtered_list = [num for num in numbers if num > smallest]
    
    # Check if there are at least 10 elements left in the filtered list
    if len(filtered_list) < 10:
        return None
    
    # Find the second smallest element in the filtered list
    second_smallest = min(filtered_list)
    
    # Return the second smallest element
    return second_smallest
