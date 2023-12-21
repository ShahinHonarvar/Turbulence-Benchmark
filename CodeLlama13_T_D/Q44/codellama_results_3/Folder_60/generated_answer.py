
def composite_nums_between_indices(numbers):
    # Create a set to store the composite numbers
    composite_nums = set()
    
    # Iterate through the list of positive integers
    for i in range(len(numbers)):
        # Check if the current number is greater than 29 and less than or equal to 51
        if numbers[i] > 29 and numbers[i] <= 51:
            # Iterate through all the factors of the current number
            for j in range(1, numbers[i] + 1):
                # If the factor is not 1 or the number itself, add it to the set
                if j != 1 and j != numbers[i]:
                    composite_nums.add(numbers[i])
    
    return composite_nums
