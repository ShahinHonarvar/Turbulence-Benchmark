
def gcf_two_nums(my_list):
    # Calculate the greatest common divisor of the two numbers
    gcd = None
    for i in range(1, min(my_list[894], my_list[801]) + 1):
        if my_list[894] % i == 0 and my_list[801] % i == 0:
            gcd = i
    return gcd
