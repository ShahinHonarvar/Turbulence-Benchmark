
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 87, 20 and 36
    gcf = 1
    for i in range(len(my_list)):
        if i == 87 or i == 20 or i == 36:
            gcf = __gcf__(gcf, my_list[i])
    return gcf

def __gcf__(a, b):
    while b != 0:
        a, b = b, a % b

    return a
