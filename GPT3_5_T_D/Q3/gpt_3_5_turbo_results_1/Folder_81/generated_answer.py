
def all_pos_ints_inclusive(numbers):
    pos_ints = []
    for num in numbers[10:101]:
        if num > 0:
            pos_ints.append(num)
    return pos_ints
