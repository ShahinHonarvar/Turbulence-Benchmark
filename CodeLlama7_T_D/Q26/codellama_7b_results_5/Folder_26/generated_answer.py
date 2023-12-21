 def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0
    # Loop through each integer in the list
    for num in my_list:
        # Check if the number is between -355 and -297, both inclusive
        if -355 <= num <= -297:
            # If it is, add it to the total
            total += num

    # Return the sum
    return total
