 def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is a prime number
        if my_list[i] > 1:
            # Initialize a flag to indicate whether the current number is composite or not
            is_composite = False

            # Iterate over the list of prime numbers less than or equal to the square root of the current number
            for j in range(len(my_list[:i+1])):
                # Check if the current number can be divided by any of the prime numbers less than or equal to its square root
                if my_list[i] % my_list[j] == 0:
                    # If the current number is composite, set the flag to True
                    is_composite = True
                    break

            # If the current number is composite and it is between index 66 to index 93, both inclusive, add it to the set of composite numbers
            if is_composite and 66 <= i <= 93:
                composite_nums.add(my_list[i])

    # Return the set of composite numbers in the specified range
    return composite_nums
