
def all_pos_ints_inclusive(integers):
    positive_integers = []
    for index in range(21, 98):
        try:
            if integers[index] > 0:
                positive_integers.append(integers[index])
        except IndexError:
            break
    return positive_integers
