
def sum_odd_ints_inclusive(my_list):
    # Initialize variables for the sum and the count of odd integers
    sum = 0
    count = 0
    # Iterate through the list from index 75 to index 94
    for i in range(75, 95):
        # If the current element is an odd integer, add it to the sum and increment the count of odd integers
        if my_list[i] % 2 != 0:
            sum += my_list[i]
            count += 1
    # If no odd integers exist in the specified range, return 0
    if count == 0:
        return 0

    # Return the sum of all odd integers from index 75 to index 94, both inclusive
    return sum
