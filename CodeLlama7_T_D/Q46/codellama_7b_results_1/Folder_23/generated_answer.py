
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 31, 25 and 80
    gcf = my_list[31]
    for i in range(len(my_list)):
        if my_list[i] != 0:
            gcf = gcf.__gcd__(my_list[i])
    return gcf
