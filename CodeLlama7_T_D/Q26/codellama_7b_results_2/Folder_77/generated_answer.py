
def sum_in_range(my_list):
    # Initialize the sum variable
    total = 0

    # Iterate through the list of integers
    for num in my_list:
        # Check if the number is between 136 and 618, both inclusive
        if 136 <= num <= 618:
            # If it is, add it to the total sum
            total += num

    # Return the total sum
    return total
