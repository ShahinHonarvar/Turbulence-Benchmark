
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # by dividing both numbers by their greatest common divisor

    num1 = my_list[56]
    num2 = my_list[92]

    gcd = 1

    while gcd > 0:
        if num1 % gcd == 0 and num2 % gcd == 0:
            break

        gcd += 1


    return gcd
