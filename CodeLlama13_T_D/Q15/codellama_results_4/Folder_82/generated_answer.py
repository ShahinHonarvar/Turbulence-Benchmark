
def sum_odd_ints_inclusive(my_list):
    total = 0
    for i in range(20, 201, 2):
        if i in my_list:
            total += my_list[i]
    return total
