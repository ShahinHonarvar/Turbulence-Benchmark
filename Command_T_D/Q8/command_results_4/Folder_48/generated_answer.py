def all_even_ints_exclusive(int_list):
    result = []
    for i in range(385, 1000):
        if i % 2 == 0:
            result.append(i)
    return result
