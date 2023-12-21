
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    div_ints = []

    # Loop through the specified range of indices in the input list
    for i in range(10, 100 + 1):

        # Check if the current integer is divisible by both 10 and 100
        if my_list[i] % 10 == 0 and my_list[i] % 100 == 0:

            # If it is, add it to the list of divisible integers
            div_ints.append(my_list[i])

    # Return the list of all integers divisible by both 10 and 100 from index 10 to index 100, both inclusive
    return div_ints
