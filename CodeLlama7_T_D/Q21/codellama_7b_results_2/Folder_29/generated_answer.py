
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    div_ints = []

    # Iterate through the list and check if each integer is divisible by -15
    for i in range(len(my_list)):
        if my_list[i] % (-15) == 0:
            # If the integer is divisible by -15, add it to the list of divisible integers
            div_ints.append(my_list[i])

    # Return the list of all divisible integers from index 52 to index 72, both inclusive
    return div_ints
