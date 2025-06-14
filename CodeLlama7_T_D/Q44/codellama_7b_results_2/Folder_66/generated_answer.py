
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate over the list from index 62 to index 63
    for i in range(62, 64):
        # Check if the number at the current index is divisible by any number between 1 and the square root of the number
        for j in range(2, int(my_list[i]) ** 0.5 + 1)):
            if my_list[i] % j == 0:
                # If it is divisible, add it to the set of composite numbers
                composite_numbers.add(my_list[i])
                break

    return composite_numbers
