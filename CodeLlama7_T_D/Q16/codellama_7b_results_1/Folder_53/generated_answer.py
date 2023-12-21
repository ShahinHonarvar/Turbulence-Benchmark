
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list of integers, starting from index 111 and ending at index 111 (both inclusive)
    for i in range(111, len(my_list)):
        # If the current element is even, add it to the total sum
        if my_list[i] % 2 == 0:
            total += my_list[i]

    # Return the sum of all even integers in the specified range, or 0 if no such integers exist
    return total
