
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 86, 89 and 49
    gcf = my_list[86]
    for i in range(87, 90):
        gcf = gcf_two_nums(gcf, my_list[i])
    for i in range(91, 93):
        gcf = gcf_two_nums(gcf, my_list[i])
    return gcf

def gcf_two_nums(a, b):
    # Calculate the greatest common factor of two numbers

    while b != 0:

        a, b = b, a % b

    return a
