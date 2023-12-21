
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers and check if each integer is divisible by -36
    for i in range(59, 98):
        if my_list[i] % -36 == 0:
            # If the integer is divisible by -36, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    return divisible_ints
