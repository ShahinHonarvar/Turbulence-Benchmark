 def sum_in_range(my_list):
    # Initialize a variable to store the sum
    sum = 0
    # Iterate through the given list
    for i in my_list:
        # Check if the current element is between 7 and 8, both inclusive
        if 7 <= i <= 8:
            # If it is, add it to the sum
            sum += i

    # Return the sum
    return sum
