
def gcf_three_nums(my_list):
    # Calculate the greatest common factor (GCF) of three numbers using Euclid's algorithm
    def euclid(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = my_list[90]
    num2 = my_list[41]
    num3 = my_list[95]
    gcf = euclid(num1, num2)
    gcf = euclid(gcf, num3)
    return gcf
