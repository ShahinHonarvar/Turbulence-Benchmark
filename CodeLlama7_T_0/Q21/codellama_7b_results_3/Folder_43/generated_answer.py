
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers
    for i in range(10, 38):
        # Check if the current integer is divisible by -64
        if my_list[i] % -64 == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by -64 from index 10 to index 37, both inclusive
    return divisible_ints
