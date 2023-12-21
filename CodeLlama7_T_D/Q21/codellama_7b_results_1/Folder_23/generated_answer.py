
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers, starting from index 59 and ending at index 97 (both inclusive)
    for i in range(59, 98):
        # Check if the current integer is divisible by -36
        if my_list[i] % -36 == 0:
            # If it is divisible, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by -36 from index 59 to index 97 (both inclusive), or an empty list if no such integers exist in the specified range
    return divisible_ints
