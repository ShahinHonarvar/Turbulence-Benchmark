
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_integers = []

    # Iterate through the list of integers
    for i in range(31, 92 + 1):

        # Check if the current integer is divisible by 20
        if my_list[i] % 20 == 0:

            # If yes, add it to the list of divisible integers
            divisible_integers.append(my_list[i])

    # Return the list of all integers divisible by 20 from index 31 to index 92, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
    return divisible_integers
