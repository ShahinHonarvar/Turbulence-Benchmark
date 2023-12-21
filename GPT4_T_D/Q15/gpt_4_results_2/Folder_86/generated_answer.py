
def sum_odd_ints_inclusive(int_list):
    sum = 0
    for i in range(31, 35):
        if i<len(int_list) and int_list[i] % 2 != 0:
            sum += int_list[i]
    return sum
