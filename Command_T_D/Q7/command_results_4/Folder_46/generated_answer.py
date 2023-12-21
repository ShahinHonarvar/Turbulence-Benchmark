
def all_even_ints_inclusive(ints):
    result = []
    for i in range(30,87):
        if int(i) % 2 == 0:
            result.append(ints[i])
    return result
