
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate through the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is between index 59 and index 97 (inclusive)
        if 59 <= i <= 97:
            # Check if the current number is composite
            if my_list[i] != 1 and my_list[i] % my_list[i-1] == 0:
                # If the current number is composite, add it to the set of composite numbers
                composite_numbers.add(my_list[i])

    # Return the set of all composite numbers between index 59 and index 97 (inclusive), or an empty set if no such numbers exist
    return composite_numbers
