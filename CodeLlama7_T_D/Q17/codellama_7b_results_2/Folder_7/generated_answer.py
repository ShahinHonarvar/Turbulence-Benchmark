
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the specified range of the input list

    for i in range(543, 584 + 1):

        # Check if the current element is divisible by both -553 and -737

        if my_list[i] % (-553) == 0 and my_list[i] % (-737) == 0:

            # If it is divisible, add it to the list of divisible integers

            divisible_ints.append(my_list[i])

    return divisible_ints
