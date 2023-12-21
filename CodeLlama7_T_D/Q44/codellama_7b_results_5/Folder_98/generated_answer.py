
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Loop through the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is a prime number
        if my_list[i] > 1:
            # Initialize a variable to store the number of factors
            num_factors = 0

            # Loop through the remaining numbers in the list
            for j in range(i + 1, len(my_list)):
                # Check if the current number is a factor of the prime number
                if my_list[j] % my_list[i] == 0:
                    # Increment the number of factors by 1
                    num_factors += 1

            # If the number of factors is greater than 2, it means that the current prime number has at least one factor other than itself and 1. Therefore, it is not a composite number.
            if num_factors <= 2:
                # Add the current prime number to the set of composite numbers
                composite_numbers.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 0 to index 6, both inclusive. If no composite number exists in the specified range, the function should return an empty set.
    return composite_numbers
