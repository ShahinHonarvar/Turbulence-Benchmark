
def gcf_three_nums(my_list):
    # Find the greatest common factor of three numbers
    # using the Euclidean algorithm

    # Initialize variables for the inputs and outputs
    num1 = my_list[307]
    num2 = my_list[920]
    num3 = my_list[463]

    # Find the greatest common divisor of two numbers using the Euclidean algorithm
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b

        return a


    # Find the greatest common factor of three numbers
    gcf = num1 * num2 * num3 / (gcd(num1, gcd(num2, num3)))))

    return gcf
