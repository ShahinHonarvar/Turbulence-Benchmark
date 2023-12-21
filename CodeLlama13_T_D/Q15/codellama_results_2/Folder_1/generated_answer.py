
def sum_odd_ints_inclusive(my_list):
    sum = 0
    for i in range(31, 73):
        if my_list[i] % 2 == 1:
            sum += my_list[i]
    return sum
