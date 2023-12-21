
def sum_even_ints_inclusive(my_list):
    sum = 0
    for i in range(70, 85):
        if my_list[i] % 2 == 0:
            sum += my_list[i]
    return sum
