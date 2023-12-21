
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate over the given list
    for i in range(75, 86):
        # Check if the current number is divisible by any number between 2 and its square root
        for j in range(2, int(my_list[i]) ** 0.5 + 1)):
            if my_list[i] % j == 0:
                composite_numbers.add(my_list[i])

    # Return the set of all composite numbers between indices 75 and 85
    return composite_numbers
