
def gcf_three_nums(my_list):
    # Find the greatest common factor of three numbers in a list
    num1 = my_list[74]
    num2 = my_list[60]
    num3 = my_list[28]
    # Calculate the greatest common divisor (GCD) of two numbers using the Euclidean algorithm
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Find the GCF of three numbers using the Euclidean algorithm
    gcf = num1

    for i in range(2, 3):
        gcf = gcd(gcf, num2 ** (i - 1))

    return gcf
