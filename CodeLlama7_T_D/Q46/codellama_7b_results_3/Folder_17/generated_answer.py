
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 20, 51 and 62
    index_20 = my_list[20]
    index_51 = my_list[51]
    index_62 = my_list[62]
    gcf = _gcf(index_20, index_51, index_62)
    return gcf
def _gcf(a, b, c):
    # Helper function to calculate the greatest common factor of three integers

    if a == 0:
        return b

    if b == 0:
        return c

    while True:
        if a % b == 0 and b % c == 0:
            return b
