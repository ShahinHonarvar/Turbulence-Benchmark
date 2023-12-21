
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers, starting from index 69 to index 70, both inclusive
    for i in range(69, 71):
        # Check if the current integer is divisible by both 72 and 70
        if my_list[i] % 72 == 0 and my_list[i] % 70 == 0:
            # If it is divisible, append it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both 72 and 70 from index 69 to index 70, both inclusive
    return divisible_ints
