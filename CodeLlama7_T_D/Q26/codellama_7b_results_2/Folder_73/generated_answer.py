 def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list of integers
    for num in my_list:
        # Check if the number is between 20 and 93, both inclusive
        if (num >= 20) and (num <= 93):
            # If it is, add it to the total
            total += num

    # Return the sum of all integers between 20 and 93, both inclusive
    return total
