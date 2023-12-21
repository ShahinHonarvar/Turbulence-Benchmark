
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers starting from index 23 to index 65, both inclusive
    for i in range(23, 65 + 1):
        # Check if the current integer is divisible by -46
        if my_list[i] % -46 == 0:
            # If it is divisible, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by -46 from index 23 to index 65, both inclusive
    return divisible_ints
