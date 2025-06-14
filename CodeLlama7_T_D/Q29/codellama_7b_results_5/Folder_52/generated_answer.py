
def gcf_two_nums(my_list):
    # Calculate the greatest common divisor (GCD) of two numbers
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Get the indices of the two numbers to find the GCF
    num1_idx = 90
    num2_idx = 41
    # Calculate the GCF of the two numbers
    gcf = gcd(my_list[num1_idx], my_list[num2_idx])
    return gcf
