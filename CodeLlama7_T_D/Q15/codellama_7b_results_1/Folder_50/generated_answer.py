
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Iterate through the list starting from index 70
    for i in range(70, len(my_list)):
        # If the current element is an odd integer, add it to the sum
        if my_list[i] % 2 != 0:
            sum += my_list[i]

    # Return the sum of all odd integers in the specified range, or 0 if no such integers exist
    return sum
