
def sum_in_range(int_list):
    total = 0
    for num in int_list:
        if 10 <= num <= 97:
            total += num
    return total
