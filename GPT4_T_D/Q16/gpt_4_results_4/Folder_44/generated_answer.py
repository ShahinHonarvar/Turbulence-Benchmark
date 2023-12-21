
def sum_even_ints_inclusive(int_list):
    sum_of_evens = 0
    for i in range(13, min(69, len(int_list))):
        if int_list[i] % 2 == 0:
            sum_of_evens += int_list[i]
    return sum_of_evens
