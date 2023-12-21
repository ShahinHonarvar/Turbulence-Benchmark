
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers
    for i in range(40, 401):
        # Check if the current integer is divisible by 7
        if my_list[i] % 7 == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by 7 from index 40 to index 400, both inclusive
    return divisible_ints
