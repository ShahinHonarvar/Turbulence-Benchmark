
def sum_in_range(int_list):
    total = 0
    for num in int_list:
        if -100 <= num <= -55:
            total += num
    return total
