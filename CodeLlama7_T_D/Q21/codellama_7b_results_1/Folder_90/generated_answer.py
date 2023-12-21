
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list and check if each integer is divisible by -173
    for i in range(len(my_list)):
        if my_list[i] % -173 == 0:
            # If the integer is divisible by -173, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by -173 from index 417 to index 890, both inclusive
    return divisible_ints
