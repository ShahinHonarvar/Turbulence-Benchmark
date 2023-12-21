
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # by dividing both numbers by their least common multiple

    # Get the indices of the two numbers to find the GCF for
    num1_idx = 83
    num2_idx = 14

    # Get the values of the two numbers
    num1 = my_list[num1_idx]
    num2 = my_list[num2_idx]

    # Find the least common multiple of the two numbers
    lcm = (num1 * num2) // math.gcd(num1, num2)

    # Divide both numbers by their least common multiple to find the GCF
    gcf = num1 // lcm
    gcf = num2 // lcm

    return gcf
