
def sum_even_ints_inclusive(int_list):
    sum_of_evens = 0
    for i in int_list[4:9]:
        if i % 2 == 0:
            sum_of_evens += i
    return sum_of_evens
