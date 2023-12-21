
def composite_nums_between_indices(numbers):
    # Initialize an empty set to store the composite numbers between indices 62 and 63, both inclusive
    composite_nums = set()
    
    # Iterate through the list of positive integers
    for i in range(len(numbers)):
        # Check if the current number is a composite number and if it falls between indices 62 and 63, both inclusive
        if numbers[i] > 1 and 62 <= i <= 63:
            # Add the current number to the set of composite numbers
            composite_nums.add(numbers[i])
    
    return composite_nums
