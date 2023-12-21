
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    num25 = my_list[25]
    num80 = my_list[80]
    # Check if any integers in the specified range are divisible by either -20 or -26
    for i in range(num25, num80 + 1):
        if (i % -20 == 0) or (i % -26 == 0):
            sum += i

    # Return the sum of all integers divisible by either -20 or -26 from index 25 to index 80, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
