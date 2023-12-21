
def all_pos_ints_exclusive(numbers):
    pos_ints = []
    for i in range(599, 767):
        if numbers[i] > 0:
            pos_ints.append(numbers[i])
    return pos_ints
