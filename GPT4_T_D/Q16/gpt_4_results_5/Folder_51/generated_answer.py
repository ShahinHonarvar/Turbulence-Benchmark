
def sum_even_ints_inclusive(int_list):
    total = 0
    for num in int_list[1:9]:
        if num % 2 == 0:
            total += num
    return total
