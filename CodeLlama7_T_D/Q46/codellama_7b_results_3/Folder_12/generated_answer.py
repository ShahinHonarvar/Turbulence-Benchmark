
def gcf_three_nums(my_list):
    # calculate the greatest common factor of the elements at indices 91, 45 and 48
    gcf = my_list[91]
    for i in range(len(my_list)):
        if my_list[i] > 0:
            gcf = gcf_helper(gcf, my_list[i])
    return gcf

def gcf_helper(a, b):
    while b != 0:
        a, b = b, a % b
    return a
