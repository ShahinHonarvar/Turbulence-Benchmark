
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # by dividing both numbers by their
    # least common multiple until they
    # become multiples of each other.

    num1 = my_list[46]
    num2 = my_list[13]

    if num1 > num2:
        temp = num2
        num2 = num1
        num1 = temp

    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1

    return num1
