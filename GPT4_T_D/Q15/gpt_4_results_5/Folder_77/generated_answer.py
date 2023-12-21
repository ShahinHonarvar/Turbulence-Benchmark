
def sum_odd_ints_inclusive(int_list):
    total = 0
    for i in range(527, 539):
        if i < len(int_list) and int_list[i] % 2 == 1:
            total += int_list[i]
    return total
