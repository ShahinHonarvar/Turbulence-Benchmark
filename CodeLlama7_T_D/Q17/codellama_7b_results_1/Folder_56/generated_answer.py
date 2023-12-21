
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list and check if each integer is divisible by both -9 and -7
    for i in range(7, 10):
        if my_list[i] % (-9 * -7) == 0:
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both -9 and -7 from index 7 to index 9, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
    return divisible_ints
