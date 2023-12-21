
def sum_odd_ints_inclusive(int_list):
    sum = 0
    for num in int_list[82:87]:
        if num % 2 != 0:
            sum += num
    return sum
