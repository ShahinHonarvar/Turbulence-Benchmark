
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 64, 80 and 15
    index_list = [64, 80, 15]
    gcf = my_list[index_list[0]]
    for i in range(1, len(index_list)):
        gcf = gcd(gcf, my_list[index_list[i]])
    return gcf
