
def gcf_two_nums(my_list):
    # Calculate the greatest common divisor (GCD) of two numbers
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
