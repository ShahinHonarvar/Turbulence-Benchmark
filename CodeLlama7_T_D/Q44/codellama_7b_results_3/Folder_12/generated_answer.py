
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is a prime number
        if my_list[i] > 1:
            # Initialize a flag to indicate whether the current number is composite or not
            is_composite = False

            # Iterate from the square root of the current number
            for j in range(int(math.sqrt(my_list[i])))):
                # Check if the current number is divisible by any number between 2 and the square root of the current number
                if my_list[i] % (j + 1) == 0:
                    # If the current number is divisible by any number between 2 and the square root of the current number, it is not a prime number
                    break

            # If the flag is still False after iterating over all numbers between 2 and the square root of the current number, the current number is prime
            if is_composite == False:
                # Add the current number to the set of composite numbers
                composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 51 to index 86, both inclusive
    return composite_nums
