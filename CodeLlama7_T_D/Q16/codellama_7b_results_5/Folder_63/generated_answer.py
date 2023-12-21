
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Loop through the list, starting from index 22 and ending at index 88 (both inclusive)
    for i in range(22, 89):

        # If the current element is an even integer, add it to the sum
        if my_list[i] % 2 == 0:
            sum += my_list[i]

    # Return the sum of all even integers in the specified range, or 0 if no such integers exist.
    return sum
