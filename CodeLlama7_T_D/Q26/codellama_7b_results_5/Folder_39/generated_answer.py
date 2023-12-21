
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Loop through each integer in the list
    for num in my_list:

        # Check if the number is between 10 and 79, both inclusive
        if 10 <= num <= 79:

            # If it is, add it to the sum
            sum += num

    # Return the sum
    return sum
