
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate over the list from index 25 to 59, inclusive
    for i in range(25, 60):
        # Check if the current element is divisible by any number between 1 and its square root (inclusive)
        for j in range(1, int(my_list[i]) ** 0.5 + 1)):
            if my_list[i] % j == 0:
                # If it is divisible by a number other than itself and 1, then it is not prime
                break

        # If the current element has been fully processed without finding any factors, then it is prime
        else:
            composite_numbers.add(my_list[i])

    # Return the set of all composite numbers found in the specified range
    return composite_numbers
