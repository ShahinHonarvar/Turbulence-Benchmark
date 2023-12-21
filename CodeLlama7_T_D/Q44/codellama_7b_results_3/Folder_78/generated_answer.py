 def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Loop through the list of positive integers
    for i in range(70, 85):
        # Check if the current number is a prime number
        if my_list[i] == 1:
            # If it's a prime number, add it to the set of composite numbers
            composite_numbers.add(my_list[i])

    return composite_numbers
