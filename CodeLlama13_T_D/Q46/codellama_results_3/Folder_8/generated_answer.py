
def gcf_three_nums(list_of_positive_integers):
    gcf = 1
    for i in range(99, 100):
        gcf *= list_of_positive_integers[i]
    return gcf
