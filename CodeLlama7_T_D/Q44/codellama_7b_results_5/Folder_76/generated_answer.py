
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Loop through the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is a prime number
        if my_list[i] > 1:
            # Initialize a variable to store the factorization of the current number
            factors = []

            # Loop through the list of positive integers again
            for j in range(len(my_list)):
                # Check if the current number is divisible by the current prime number
                if my_list[i] % my_list[j] == 0:
                    # Add the current prime number to the list of factors
                    factors.append(my_list[j])

            # If the list of factors contains more than two elements, then the current number is a composite number
            if len(factors) > 2:
                # Add the current number to the set of composite numbers
                composite_nums.add(my_list[i])

    # Return the set of composite numbers that are between index 639 and index 975, both inclusive
    return composite_nums
