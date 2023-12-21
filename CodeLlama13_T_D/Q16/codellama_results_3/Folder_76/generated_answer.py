
def sum_even_ints_inclusive(my_list):
    # initialize a variable to store the sum
    sum = 0
    # loop through the list and check if each element is even
    for i in range(686, 988):
        if my_list[i] % 2 == 0:
            # if it is even, add it to the sum
            sum += my_list[i]
    return sum
