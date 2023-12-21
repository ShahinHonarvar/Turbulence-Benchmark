
def gcf_two_nums(my_list):
    # Calculate the greatest common factor (gcf) of two numbers using the Euclidean algorithm
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Return the gcf of the two specified indices in the list
    return gcf(my_list[17], my_list[20])
