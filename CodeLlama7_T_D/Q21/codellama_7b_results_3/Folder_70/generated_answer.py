
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    div_ints = []

    # Iterate through the list of integers
    for i in range(70, 72):
        # Check if the current integer is divisible by 85
        if my_list[i] % 85 == 0:
            # If so, add it to the list of divisible integers
            div_ints.append(my_list[i])

    # Return the list of all integers divisible by 85 from index 70 to index 71, both inclusive
    return div_ints
