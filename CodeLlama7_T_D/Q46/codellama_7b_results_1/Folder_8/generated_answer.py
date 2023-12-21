
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 99, 28 and 53
    index_1 = my_list[99]
    index_2 = my_list[28]
    index_3 = my_list[53]
    gcf = _gcf(index_1, index_2, index_3)
    return gcf

def _gcf(a, b, c):
    # Calculate the greatest common factor of two numbers using the Euclid's algorithm
    while b != 0:
        a, b = b, a % b

    if c % a == 0:
        return a

    else:
        return _gcf(a, c % a)
