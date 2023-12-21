
def sum_odd_ints_inclusive(int_list):
    sum_odd = 0
    for i in int_list[8:10]:
        if i % 2 != 0:
            sum_odd += i
    return sum_odd
