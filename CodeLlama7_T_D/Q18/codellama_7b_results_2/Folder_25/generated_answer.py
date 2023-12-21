
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    num1 = -20
    num2 = -26

    # Iterate over the list starting from index 25 to index 80, both inclusive
    for i in range(25, 81):
        # Check if the current element is divisible by either num1 or num2
        if my_list[i] % num1 == 0 or my_list[i] % num2 == 0:
            # Add the current element to the sum
            sum += my_list[i]

    # Return the sum of all integers divisible by either -20 or -26 from index 25 to index 80, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
