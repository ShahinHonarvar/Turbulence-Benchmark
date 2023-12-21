
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the list of positive integers
    for i in range(10, 101):
        # Check if the current number is divisible by any number between 2 and the square root of the current number
        if any(my_list[i] % my_list[j] == 0 for j in range(2, int(math.sqrt(my_list[i])) + 1))):
            # If it is divisible by any number, add it to the set of composite numbers
            composite_nums.add(my_list[i])
    return composite_nums
