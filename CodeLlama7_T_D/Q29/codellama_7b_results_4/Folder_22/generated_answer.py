
def gcf_two_nums(my_list):
    # Calculate the greatest common factor (GCF) of two numbers
    # The function takes a list of positive integers as input
    # It returns the GCF of the integers at indices 24 and 68 in the list
    # First, we find the indices of the two numbers whose GCF we want to calculate
    num1_index = my_list.index(24)
    num2_index = my_list.index(68)
    # Next, we extract the two numbers from the list using their indices
    num1 = my_list[num1_index]
    num2 = my_list[num2_index]
    # We then find the GCF of the two numbers by dividing both numbers by their greatest common divisor (GCD)
    gcd = _get_gcd(num1, num2)
    gcf = num1 * num2 / gcd
    return gcf

def _get_gcd(a, b):
    # This function calculates the greatest common divisor (GCD) of two positive integers
    # It returns the GCD as an integer value

    if a == 0:
        return b

    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    return a
