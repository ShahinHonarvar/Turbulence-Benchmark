
def gcf_two_nums(my_list):
    # Calculate the greatest common factor (GCF) of two numbers
    # Use the Euclidean algorithm to find the GCF of two numbers
    a = my_list[4]
    b = my_list[0]
    while b != 0:
        a, b = b, a % b
    return a
