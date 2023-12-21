
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 4, 0 and 8
    gcf = my_list[4]
    for i in range(5, 9):
        gcf = gcf_helper(gcf, my_list[i])
    return gcf

def gcf_helper(a, b):
    # Calculate the greatest common factor of two numbers

    while b != 0:
        a, b = b, a % b

    return a
