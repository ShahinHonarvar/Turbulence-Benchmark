
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 20, 43 and 95
    gcf = my_list[20]
    for i in range(21, 43):
        gcf = gcf_two_nums(gcf, my_list[i])
    for i in range(43, 95):
        gcf = gcf_two_nums(gcf, my_list[i])
    return gcf

def gcf_two_nums(a, b):
    # Calculate the greatest common factor of two numbers

    while b != 0:

        a, b = b, a % b

    return a
