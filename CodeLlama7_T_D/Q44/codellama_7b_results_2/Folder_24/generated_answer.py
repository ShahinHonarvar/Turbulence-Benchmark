
def composite_nums_between_indices(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list)):
        raise TypeError("Input must be a list")
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()
    # Loop through the list and check for each element whether it is a prime number or not
    for i in range(len(my_list))):
        if my_list[i] > 1:
            for j in range(2, my_list[i]):
                if my_list[i] % j == 0:
                    composite_numbers.add(my_list[i])
    # Return the set of all composite numbers between index 34 and index 55
    return composite_numbers
