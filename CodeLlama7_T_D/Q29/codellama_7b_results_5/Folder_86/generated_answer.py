
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of the two numbers
    gcf = 1
    for i in range(2, min(my_list[793], my_list[449]) + 1)):
        if my_list[793] % i == 0 and my_list[449] % i == 0:
            gcf = i
    return gcf
