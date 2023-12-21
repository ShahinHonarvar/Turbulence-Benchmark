
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers
    for i in range(10, 56 + 1):
        # Check if the current integer is divisible by 16
        if my_list[i] % 16 == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by 16 from index 10 to index 56, both inclusive
    return divisible_ints
