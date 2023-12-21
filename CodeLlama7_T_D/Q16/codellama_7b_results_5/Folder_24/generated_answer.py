
def sum_even_ints_inclusive(my_list):
    # Define the start and end indices for the range we want to sum
    start_index = 74
    end_index = 95
    # Initialize a variable to store the sum
    total = 0
    # Iterate through the list within the specified range
    for i in range(start_index, end_index + 1):
        # If the current element is even, add it to the total
        if my_list[i] % 2 == 0:
            total += my_list[i]
    return total
