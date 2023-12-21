
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    div_ints = []

    # Iterate over the specified range of the input list
    for i in range(66, 75):
        # Check if the current element is divisible by -14
        if my_list[i] % -14 == 0:
            # If it is divisible, add it to the list of divisible integers
            div_ints.append(my_list[i])

    # Return the list of divisible integers
    return div_ints
