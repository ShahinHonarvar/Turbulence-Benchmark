 def sum_even_ints_inclusive(my_list):
    start = 209
    end = 556
    even_ints = []
    for i in range(start, end + 1):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return sum(even_ints)
