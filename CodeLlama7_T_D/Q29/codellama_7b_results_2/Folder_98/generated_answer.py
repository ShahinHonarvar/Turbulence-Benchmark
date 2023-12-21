
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # by dividing both numbers by their least common multiple

    num1 = my_list[0]
    num2 = my_list[9]

    lcm = num1 * num2 / gcf(num1, num2)

    return gcf(num1 // lcm, num2 // lcm)

def gcf(a, b):

    # Euclidean algorithm for finding the greatest common divisor of two numbers

    while b:
        a, b = b, a % b

    return a
