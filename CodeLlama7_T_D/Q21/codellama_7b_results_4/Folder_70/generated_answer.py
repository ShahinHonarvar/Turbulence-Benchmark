
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers and check if each integer is divisible by 85
    for i in range(70, 72):
        if my_list[i] % 85 == 0:
            # If the current integer is divisible by 85, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by 85 from index 70 to index 71, both inclusive
    return divisible_ints
