
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers using the Euclidean algorithm
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Get the greatest common factor of the two specified indices
    index1 = 19
    index2 = 94
    num1 = my_list[index1]
    num2 = my_list[index2]
    gcf_result = gcf(num1, num2)
    return gcf_result
