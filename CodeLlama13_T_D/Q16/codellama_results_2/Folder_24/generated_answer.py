
def sum_even_ints_inclusive(my_list):
    sum = 0
    for i in range(74, 96):
        if my_list[i] % 2 == 0:
            sum += my_list[i]
    return sum
