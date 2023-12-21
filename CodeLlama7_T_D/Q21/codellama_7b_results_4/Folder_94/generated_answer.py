
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    div_ints = []

    # Iterate through the specified range of the input list
    for i in range(18, 93 + 1):
        # Check if the current element is divisible by -85
        if my_list[i] % -85 == 0:
            # If it is, add it to the list of divisible integers
            div_ints.append(my_list[i])

    # Return the list of all integers divisible by -85 from index 18 to index 93, both inclusive
    return div_ints
