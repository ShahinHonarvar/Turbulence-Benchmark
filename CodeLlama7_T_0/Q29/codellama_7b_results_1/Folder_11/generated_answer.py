
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # by dividing both numbers by their
    # least common multiple

    num1 = my_list[64]
    num2 = my_list[80]

    lcm = (num1 * num2) // math.gcd(num1, num2)

    gcf = 1

    for i in range(2, lcm + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i

    return gcf
