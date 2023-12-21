
def composite_nums_between_indices(my_list):
    # Define the starting and ending indices for the range
    start_index = 62
    end_index = 99
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Loop through the list of positive integers
    for i in my_list:
        # Check if the current number is a prime number
        if is_prime(i):
            continue

        # Check if the current number is between the starting and ending indices
        if start_index <= i <= end_index:
            # Add the current number to the set of composite numbers
            composite_numbers.add(i)

    return composite_numbers
