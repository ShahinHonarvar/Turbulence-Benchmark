
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # by dividing both numbers by their
    # least common multiple until it reaches 1

    num1 = my_list[96]
    num2 = my_list[57]

    if num1 < num2:
        temp = num1
        num1 = num2
        num2 = temp

    while num1 != 1:
        if num1 % num2 == 0:
            num1 = num1 // num2
        else:
            num2 = num2 // num1

    return num1
