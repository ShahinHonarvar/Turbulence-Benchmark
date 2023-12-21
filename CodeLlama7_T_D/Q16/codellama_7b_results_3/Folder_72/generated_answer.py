 def sum_even_ints_inclusive(my_list):
    even_ints = []
    for i in range(29, 51 + 1):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return sum(even_ints)
