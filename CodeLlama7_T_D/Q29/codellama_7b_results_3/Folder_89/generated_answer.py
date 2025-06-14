
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # by dividing both numbers by their least common multiple

    num1 = my_list[37]
    num2 = my_list[30]

    lcm = (num1 * num2) // math.gcd(num1, num2)

    gcf = 1

    while gcf <= lcm:
        if num1 % gcf == 0 and num2 % gcf == 0:
            break

        gcf += 1

    return gcf
