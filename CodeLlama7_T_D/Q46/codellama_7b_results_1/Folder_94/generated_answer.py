
def gcf_three_nums(my_list):
    # Find the greatest common factor of three numbers
    # using the Euclidean algorithm

    def euclid(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = my_list[56]
    num2 = my_list[88]
    num3 = my_list[51]
    gcf = euclid(num1, num2)
    gcf = euclid(gcf, num3)
    return gcf
