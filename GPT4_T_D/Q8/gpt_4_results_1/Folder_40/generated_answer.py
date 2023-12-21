
def all_even_ints_exclusive(integer_list):
    result = []
    for i in integer_list[1:2]:
        if i % 2 == 0:
            result.append(i)
    return result
