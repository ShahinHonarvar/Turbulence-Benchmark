
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list and check if each integer is divisible by both -34 and 64
    for i in range(50, 201):
        if my_list[i] % (-34 * 64) == 0:
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both -34 and 64 from index 50 to index 200, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
    return divisible_ints
