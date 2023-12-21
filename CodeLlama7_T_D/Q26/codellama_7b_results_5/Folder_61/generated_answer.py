
def sum_in_range(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list and check if each element is between 8 and 9, both inclusive
    for i in my_list:
        if 8 <= i <= 9:
            # If the element is between 8 and 9, add it to the total
            total += i

    # Return the sum of all integers from the given list that are between 8 and 9, both inclusive. If the given list does not contain such integers, the function should return 0.
    return total
