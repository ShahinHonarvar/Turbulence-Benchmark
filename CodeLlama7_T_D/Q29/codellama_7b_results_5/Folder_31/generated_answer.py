
def gcf_two_nums(my_list):
    # Calculate the greatest common factor (GCF) of two numbers
    # using the Euclidean algorithm

    a = my_list[87]
    b = my_list[95]
    while b != 0:
        temp = b
        b = a % b
        a = temp

    return a
