
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is a prime number
        if my_list[i] > 1:
            # Initialize a variable to store the factorization of the current number
            factors = []

            # Iterate over the list of positive integers again
            for j in range(len(my_list)):
                # Check if the current number is divisible by the current number in the list
                if my_list[i] % my_list[j] == 0:
                    # Add the factor to the list of factors
                    factors.append(my_list[j])

            # If the list of factors has more than two elements, it means that the current number is composite and should be added to the set of composite numbers
            if len(factors) > 2:
                composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 0 to index 5, both inclusive
    return composite_nums
