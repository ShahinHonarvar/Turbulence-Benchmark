
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is a prime number
        if my_list[i] > 1:
            # Initialize a flag to indicate whether the current number is composite or not
            is_composite = False

            # Iterate from 2 to the square root of the current number
            for j in range(2, int(my_list[i]) ** 0.5 + 1)):
                # Check if the current number is divisible by any number between 2 and the square root of the current number
                if my_list[i] % j == 0:
                    # If the current number is divisible by any number between 2 and the square root of the current number, it is not a prime number
                    is_composite = True
                    break

            # If the current number is composite, add it to the set of composite numbers
            if is_composite:
                composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 90 to index 200, both inclusive
    return composite_nums
