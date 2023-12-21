
def sum_odd_ints_inclusive(int_list):
    sum_of_odd = 0
    for elem in int_list[1:9]:
        if elem % 2 != 0:
            sum_of_odd += elem
    return sum_of_odd
