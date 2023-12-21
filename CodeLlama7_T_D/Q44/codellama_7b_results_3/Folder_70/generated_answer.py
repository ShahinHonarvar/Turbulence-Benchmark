 def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate through the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is a prime number
        if my_list[i] > 1:
            # Initialize a variable to store the current number's factor
            factor = 2
            # Loop through all possible factors of the current number
            while factor ** 2 <= my_list[i]:
                # Check if the current number is divisible by the current factor
                if my_list[i] % factor == 0:
                    # If the current number is divisible by the current factor, add it to the set of composite numbers
                    composite_nums.add(my_list[i])
                    # Break out of the loop since we have found all possible factors of the current number
                    break
                # Increment the current factor by 1
                factor += 1

            # If the current number is not a prime number, add it to the set of composite numbers
            if my_list[i] > 1:
                composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 32 to index 35, both inclusive. If no composite number exists in the specified range, the function should return an empty set.
    return composite_nums
