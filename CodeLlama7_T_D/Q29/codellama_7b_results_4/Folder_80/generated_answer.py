
def gcf_two_nums(my_list):
    # Get the greatest common factor of two numbers
    # by dividing both numbers by their
    # least common multiple (LCM) until they are equal


    num1 = my_list[95]
    num2 = my_list[85]


    lcm = 1
    while True:
        if num1 % lcm == 0 and num2 % lcm == 0:
            gcf = lcm
            break

        lcm += 1

    return gcf
