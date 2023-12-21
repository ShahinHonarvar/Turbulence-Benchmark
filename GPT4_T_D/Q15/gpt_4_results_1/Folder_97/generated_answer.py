
def sum_odd_ints_inclusive(num_list):
    return sum(num for index, num in enumerate(num_list[40:81]) if num % 2 == 1)
