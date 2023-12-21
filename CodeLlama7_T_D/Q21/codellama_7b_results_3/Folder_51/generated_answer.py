
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    div_ints = []

    # Loop through the list and check if each integer is divisible by -6
    for i in range(len(my_list)):
        if my_list[i] % (-6) == 0:
            div_ints.append(my_list[i])

    # Return the list of all divisible integers from index 5 to index 6, both inclusive
    return div_ints
