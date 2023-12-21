
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate through the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is a prime number
        if my_list[i] > 1:
            # Initialize a flag to indicate whether the current number is composite or not
            is_composite = False

            # Iterate from the square root of the current number to 1
            for j in range(int(math.sqrt(my_list[i]))), 0, -1):
                # Check if any of the numbers between the square root and 1 divide the current number without leaving a remainder
                if my_list[i] % j == 0:
                    # If yes, set the flag to True
                    is_composite = True
                    break

            # If the current number is composite, add it to the set of composite numbers
            if is_composite:
                composite_numbers.add(my_list[i])

    # Return the set of all composite numbers between index 533 and index 605, both inclusive
    return composite_numbers
