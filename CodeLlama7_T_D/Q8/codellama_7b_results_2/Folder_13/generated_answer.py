 def all_even_ints_exclusive(my_list):
    start = 73
    end = 84
    even_ints = []
    for i in range(start, end):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints
