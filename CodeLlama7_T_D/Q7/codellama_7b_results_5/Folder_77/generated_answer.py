
def all_even_ints_inclusive(my_list):
    start = 527
    end = 538
    even_ints = []
    for i in range(start, end + 1):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints
