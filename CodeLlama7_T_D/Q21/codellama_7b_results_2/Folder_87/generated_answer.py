
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers and check if each integer is divisible by 16
    for i in range(10, 57):
        if my_list[i] % 16 == 0:
            # If the integer is divisible by 16, append it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by 16 from index 10 to index 56, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
    return divisible_ints
