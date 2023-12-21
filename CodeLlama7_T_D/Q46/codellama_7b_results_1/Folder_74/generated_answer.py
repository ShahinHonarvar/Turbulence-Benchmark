
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 99, 95 and 80
    gcf = None
    for i in range(3):
        current_gcf = gcf_two_nums([my_list[99], my_list[95]])
        if gcf is None:
            gcf = current_gcf
        else:
            gcf = gcf_two_nums([gcf, current_gcf])
    return gcf

def gcf_two_nums(my_list):

    # Calculate the greatest common factor of two positive integers

    if my_list[0] > my_list[1]:
        temp = my_list[0]
        my_list[0] = my_list[1]
        my_list[1] = temp
    while my_list[0] != 0:
        remainder = my_list[1] % my_list[0]
        if remainder == 0:
            return my_list[0]
        else:
            temp = my_list[0]
            my_list[0] = remainder
            my_list[1] = temp
    return 1
