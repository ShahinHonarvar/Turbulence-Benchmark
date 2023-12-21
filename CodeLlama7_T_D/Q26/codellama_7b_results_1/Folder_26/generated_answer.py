
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list and check if each element is between -355 and -297
    for num in my_list:
        if -355 <= num <= -297:
            # If it is, add it to the sum
            total += num

    # Return the sum
    return total
