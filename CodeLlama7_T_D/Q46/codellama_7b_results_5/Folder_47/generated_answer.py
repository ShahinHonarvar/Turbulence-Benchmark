
def gcf_three_nums(my_list):
    # Find the greatest common factor of three numbers
    # using the Euclidean algorithm

    def euclid(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    num1 = my_list[36]
    num2 = my_list[85]
    num3 = my_list[83]
    gcf = euclid(num1, euclid(num2, num3))
    return gcf
