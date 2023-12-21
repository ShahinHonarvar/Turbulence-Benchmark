
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(1, len(my_list)):
        # Check if the current number is a prime number
        if my_list[i] > 1:
            # Initialize a variable to store the factorization of the current number
            factors = []

            # Iterate over the list of prime numbers less than or equal to the current number
            for j in range(len(my_list[:i])):
                # Check if the current number is divisible by the current prime number
                if my_list[i] % my_list[j] == 0:
                    # Add the factorization of the current number to the list of factors
                    factors.append(my_list[j])

            # Check if the list of factors is empty, indicating that the current number is prime
            if len(factors) == 0:
                # Add the current number to the set of composite numbers
                composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 1 to index 8, both inclusive
    return composite_nums
