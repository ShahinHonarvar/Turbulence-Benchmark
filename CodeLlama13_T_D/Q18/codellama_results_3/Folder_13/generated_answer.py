
def sum_ints_div_by_either_nums(my_list):
    # Slice the list from index 13 to index 18, both inclusive
    sliced_list = my_list[12:19]
    
    # Iterate over the sliced list and check if each integer is divisible by 45 or 20
    for num in sliced_list:
        if (num % 45 == 0) or (num % 20 == 0):
            sum += num
    
    # Return the sum of all integers divisible by either 45 or 20, or 0 if no such integers exist
    return sum
