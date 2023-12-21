
def gcf_two_nums(my_list):
    # Calculate the greatest common factor (gcf) of the two numbers
    gcf = 1
    for i in range(2, min(my_list[25], my_list[80])) + 1):
        if my_list[25] % i == 0 and my_list[80] % i == 0:
            gcf = i

    return gcf
