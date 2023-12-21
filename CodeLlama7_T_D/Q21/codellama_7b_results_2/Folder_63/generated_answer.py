
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    div_ints = []

    # Iterate through the list and check if each integer is divisible by 84
    for i in range(50, 55):
        if my_list[i] % 84 == 0:
            div_ints.append(my_list[i])

    # Return the list of divisible integers
    return div_ints
