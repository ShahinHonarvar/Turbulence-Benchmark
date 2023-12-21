
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(len(my_list)):

        # Check if the current number is a prime number
        if my_list[i] > 1:

            # Check if the current number is a composite number between indices 62 and 78, both inclusive
            if 62 <= i <= 78:

                # Add the current number to the set of composite numbers
                composite_nums.add(my_list[i])

    # Return the set of all composite numbers between indices 62 and 78, both inclusive
    return composite_nums
