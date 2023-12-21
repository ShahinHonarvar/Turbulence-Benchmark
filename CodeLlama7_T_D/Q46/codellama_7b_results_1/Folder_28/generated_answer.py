
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of three numbers
    # using the Euclidean algorithm

    def euclid(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    num1 = my_list[99]
    num2 = my_list[63]
    num3 = my_list[74]
    gcf = euclid(num1, num2)
    gcf = euclid(gcf, num3)
    return gcf
