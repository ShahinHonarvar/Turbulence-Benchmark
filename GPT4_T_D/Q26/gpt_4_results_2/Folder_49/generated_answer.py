
def sum_in_range(int_list):
    total = 0
    for num in int_list:
        if 3 <= num <= 9:
            total += num
    return total
