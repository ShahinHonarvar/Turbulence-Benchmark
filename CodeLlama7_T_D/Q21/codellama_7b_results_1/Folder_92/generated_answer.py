
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the list of integers
    for i in range(len(my_list)):
        # Check if the current integer is divisible by 1 from index 0 to index 0, both inclusive
        if my_list[i] % 1 == 0:
            # If it is divisible, append it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by 1 from index 0 to index 0, both inclusive
    return divisible_ints
