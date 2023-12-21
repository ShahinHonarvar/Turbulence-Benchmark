
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # Using the Euclidean algorithm

    def euclidean_algorithm(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    num1 = my_list[69]
    num2 = my_list[40]
    gcf = euclidean_algorithm(num1, num2)
    return gcf
