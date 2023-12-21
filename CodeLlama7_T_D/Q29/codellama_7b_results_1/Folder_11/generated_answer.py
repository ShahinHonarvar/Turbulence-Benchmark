
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # by dividing both numbers by their least common multiple

    num1 = my_list[64]
    num2 = my_list[80]

    lcm = num1 * num2 / (num1 * num2)

    gcf = 1

    while lcm % gcf != 0:
        gcf += 1

    return gcf
