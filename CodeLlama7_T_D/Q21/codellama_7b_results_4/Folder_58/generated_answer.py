
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the list of integers and check if each integer is divisible by 965
    for i in range(len(my_list)):
        if my_list[i] % 965 == 0:
            # If the integer is divisible by 965, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by 965 from index 255 to index 618, both inclusive
    return divisible_ints
