
def sum_odd_ints_inclusive(num_list):
    sum_odd = 0
    for num in num_list[533:606]:
        if num % 2 != 0:
            sum_odd += num
    return sum_odd
