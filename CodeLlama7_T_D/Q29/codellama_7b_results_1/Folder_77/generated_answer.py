
def gcf_two_nums(my_list):
    # find the greatest common factor of two numbers
    # using the Euclidean algorithm

    def euclid_algorithm(a, b):
        while b != 0:
            t = b
            b = a % b
            a = t

        return a


    num1 = my_list[841]
    num2 = my_list[804]

    gcf = euclid_algorithm(num1, num2)

    return gcf
