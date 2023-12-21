
def sum_even_ints_inclusive(my_list):
    # Iterate through the list and check if each element is even
    for i in range(527, 539):
        if my_list[i] % 2 == 0:
            return sum(my_list[i])
    return 0
