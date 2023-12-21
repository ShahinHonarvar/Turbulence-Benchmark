
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Loop through the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is a prime number
        if my_list[i] > 1:
            # Initialize a flag to indicate whether the current number is composite
            is_composite = False

            # Loop through the factors of the current number
            for j in range(2, int(my_list[i] ** 0.5) + 1):
                # Check if any of the factors is equal to 1, which means that the current number is prime
                if my_list[i] % j == 0:
                    # If any of the factors is equal to 1, set the flag to True and break out of the loop
                    is_composite = True
                    break

            # If the flag is False, it means that all the factors of the current number are greater than 1, which means that the current number is composite
            if not is_composite:
                # Add the current number to the set of composite numbers
                composite_nums.add(my_list[i])

    # Return the set of composite numbers between index 23 and index 23, both inclusive
    return composite_nums
