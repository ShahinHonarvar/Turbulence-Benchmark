 def sum_in_range(my_list):
    # Initialize a variable to store the sum
    sum = 0
    # Iterate over the list of integers
    for num in my_list:
        # Check if the current integer is between 782 and 787, both inclusive
        if 782 <= num <= 787:
            # If it is, add it to the sum
            sum += num

    # Return the sum of all integers from the given list that are between 782 and 787, both inclusive. If the given list does not contain such integers, the function should return 0.
    return sum
