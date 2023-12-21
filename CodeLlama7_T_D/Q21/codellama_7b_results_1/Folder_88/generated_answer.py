
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers and check if each integer is divisible by -8
    for i in my_list:
        if i % (-8) == 0:
            # If the integer is divisible by -8, add it to the list of divisible integers
            divisible_ints.append(i)

    return divisible_ints
