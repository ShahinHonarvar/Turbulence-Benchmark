
def find_second_smallest_num(numbers):
    # Check if the list is empty or not
    if not numbers:
        return None
    
    # Find the smallest element in the list
    smallest = min(numbers)
    
    # Find the second smallest element by iterating over the list and comparing each element to the smallest element
    for num in numbers[310:370]:
        if num < smallest:
            smallest = num
    
    return smallest
