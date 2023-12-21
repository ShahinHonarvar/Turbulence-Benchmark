
def gcf_two_nums(my_list):
    # Calculate the greatest common factor (GCF) of two numbers using the Euclidean algorithm
    def euclid_algorithm(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Get the two numbers to find their GCF
    num1 = my_list[3]
    num2 = my_list[8]
    # Find the GCF using the Euclidean algorithm
    gcf = euclid_algorithm(num1, num2)
    return gcf
