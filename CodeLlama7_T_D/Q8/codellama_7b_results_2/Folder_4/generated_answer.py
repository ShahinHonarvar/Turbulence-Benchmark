
def all_even_ints_exclusive(my_list):
    # Find the first even integer in the list
    for i in range(10, len(my_list)):
        if my_list[i] % 2 == 0:
            start = i
            break

    else:

        return []
