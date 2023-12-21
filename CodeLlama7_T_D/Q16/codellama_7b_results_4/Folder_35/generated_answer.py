
def sum_even_ints_inclusive(my_list):
    # Initialize variables
    sum = 0
    start_index = 30
    end_index = 48
    # Iterate through the list from the start index to the end index
    for i in range(start_index, end_index + 1):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # Add the current element to the sum
            sum += my_list[i]
    # Return the sum of all even integers in the specified range
    return sum
