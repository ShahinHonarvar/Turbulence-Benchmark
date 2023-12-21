
def sum_even_ints_inclusive(ints_list):
    sum = 0
    for i in range(59, 98):
        if i < len(ints_list) and ints_list[i] % 2 == 0:
            sum += ints_list[i]
    return sum
