
def sum_odd_ints_inclusive(int_list):
    sum_odd_integers = 0
    for i in range(639, 976):
        if i < len(int_list) and int_list[i] % 2 != 0:
            sum_odd_integers += int_list[i]
    return sum_odd_integers
