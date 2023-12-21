
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    div_ints = []

    # Iterate over the specified range of the input list

    for i in range(240, 901 + 1):

        # Check if the current integer is divisible by both 546 and 709

        if my_list[i] % 546 == 0 and my_list[i] % 709 == 0:

            # If it is, add it to the list of divisible integers

            div_ints.append(my_list[i])

    # Return the list of all integers divisible by both 546 and 709 from index 240 to index 901, both inclusive

    return div_ints
