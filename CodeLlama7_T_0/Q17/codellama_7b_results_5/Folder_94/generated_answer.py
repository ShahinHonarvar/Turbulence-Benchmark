
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers
    for i in range(len(my_list)):
        # Check if the current integer is divisible by both -53 and -91
        if my_list[i] % (-53) == 0 and my_list[i] % (-91) == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both -53 and -91 from index 93 to index 94, both inclusive
    return divisible_ints
