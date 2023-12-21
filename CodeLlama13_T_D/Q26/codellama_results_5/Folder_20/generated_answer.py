
def sum_in_range(my_list):
    total = 0
    for num in my_list:
        if -64 <= num <= 42:
            total += num
    return total
