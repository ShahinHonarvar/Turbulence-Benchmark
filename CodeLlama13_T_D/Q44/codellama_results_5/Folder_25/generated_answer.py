
def composite_nums_between_indices(numbers):
    # Find the indices of the 75th and 94th elements
    start_index = 75
    end_index = 94
    
    # Create an empty set to store the composite numbers
    composite_nums = set()
    
    # Iterate through the list from the 75th element to the 94th element
    for i in range(start_index, end_index + 1):
        # Check if the current element is a composite number
        if len(set(range(2, numbers[i]))) == numbers[i] - 1:
            # If it is, add it to the set of composite numbers
            composite_nums.add(numbers[i])
    
    return composite_nums
