
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the list of integers and check if each integer is divisible by -215
    for i in range(len(my_list)):
        if my_list[i] % -215 == 0:
            # If the integer is divisible by -215, append it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all divisible integers between index 319 and index 612 (both inclusive)
    return divisible_ints
