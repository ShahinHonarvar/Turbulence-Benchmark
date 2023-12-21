
def sum_even_ints_inclusive(my_list):
    even_ints = []
    for i in range(30, 201, 1):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return sum(even_ints) or 0
