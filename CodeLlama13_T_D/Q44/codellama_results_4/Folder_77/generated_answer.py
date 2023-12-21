
def composite_nums_between_indices(numbers):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    
    # Iterate through the list of positive integers
    for i, num in enumerate(numbers):
        # Check if the current number is a composite number
        if num > 1 and all(num % div != 0 for div in range(2, int(num ** 0.5) + 1)):
            # If the current number is a composite number, add it to the set
            composite_nums.add(num)
    
    # Return the set of all composite numbers between indices 667 and 774, both inclusive
    return {num for num in composite_nums if 667 <= i <= 774}
