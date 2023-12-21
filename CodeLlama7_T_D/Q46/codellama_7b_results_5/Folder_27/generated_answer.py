
def gcf_three_nums(my_list):
    # Find the greatest common factor of three numbers
    # using the Euclidean algorithm

    def euclid_gcd(a, b):
        while b != 0:
            a, b = b, a % b

        return a


    # Get the elements at indices 76, 64 and 28
    num1 = my_list[76]
    num2 = my_list[64]
    num3 = my_list[28]

    # Find the greatest common factor of these numbers
    gcf = euclid_gcd(num1, num2)
    gcf = euclid_gcd(gcf, num3)

    return gcf
