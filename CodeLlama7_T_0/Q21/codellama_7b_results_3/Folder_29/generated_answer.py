
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers
    for i in range(52, 73):
        # Check if the current integer is divisible by -15
        if my_list[i] % -15 == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by -15 from index 52 to index 72, both inclusive
    return divisible_ints
