
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list and check if each integer is divisible by 89
    for i in range(17, 64):
        if my_list[i] % 89 == 0:
            divisible_ints.append(my_list[i])

    # Return the list of all divisible integers
    return divisible_ints
