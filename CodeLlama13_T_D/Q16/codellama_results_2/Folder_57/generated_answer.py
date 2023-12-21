
def sum_even_ints_inclusive(my_list):
    start = 27
    end = 55
    total = 0
    for i in range(start, end+1):
        if my_list[i] % 2 == 0:
            total += my_list[i]
    return total
