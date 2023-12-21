
def gcf_three_nums(my_list):
    # Find the greatest common factor of three numbers at different indices in a list
    gcf = 1
    for i in range(20, 35, 74):
        gcf = gcf.__gcd__(my_list[i])
    return gcf
