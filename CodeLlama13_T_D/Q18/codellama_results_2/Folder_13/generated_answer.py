
def sum_ints_div_by_either_nums(my_list):
    # Slice the list from index 13 to index 18, both inclusive
    sliced_list = my_list[12:19]
    
    # Initialize a variable to store the sum
    sum_divisible = 0
    
    # Iterate over the sliced list and check if each element is divisible by either 45 or 20
    for num in sliced_list:
        if (num % 45 == 0) or (num % 20 == 0):
            sum_divisible += num
    
    # Return the sum of divisible integers, or 0 if no such integer exists
    return sum_divisible
