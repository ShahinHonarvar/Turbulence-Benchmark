
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
                    # Add the factorization of the current number to the set of composite numbers
                    composite_nums.add(my_list[i])

            # If the current number is not a prime number and has at least one factor, add it to the set of composite numbers
            if len(factors) > 0:
                composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 3 to index 5, both inclusive
    return composite_nums
