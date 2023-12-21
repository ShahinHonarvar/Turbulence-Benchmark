
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers

    for i in range(20, 201):

        # Check if the current integer is divisible by both -20 and -200

        if my_list[i] % (-20) == 0 and my_list[i] % (-200) == 0:

            # If it is, append it to the list of divisible integers

            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both -20 and -200 from index 20 to index 200, both inclusive

    return divisible_ints
