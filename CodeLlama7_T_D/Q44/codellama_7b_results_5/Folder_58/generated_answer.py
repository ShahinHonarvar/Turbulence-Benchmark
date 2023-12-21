
def composite_nums_between_indices(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list)):
        raise ValueError("Input must be a list")

    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate over the list of positive integers
    for i in my_list:
        if (i > 533) and (i < 605)):
            # Check if the current number is a prime number
            if is_prime(i):
                composite_numbers.add(i)

    return composite_numbers
