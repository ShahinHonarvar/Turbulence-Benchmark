
def all_ints_div_by_num(my_list):
    # Create a new list to store the divisible integers
    divisible_integers = []

    # Loop through the list of integers and check if each integer is divisible by 16
    for i in range(len(my_list)):
        if my_list[i] % 16 == 0:
            # If the integer is divisible by 16, add it to the list of divisible integers
            divisible_integers.append(my_list[i])

    # Return the list of all divisible integers in the specified range
    return divisible_integers
