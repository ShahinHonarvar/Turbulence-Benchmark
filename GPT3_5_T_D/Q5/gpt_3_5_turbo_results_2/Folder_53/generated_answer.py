
def all_neg_ints_inclusive(lst):
    negative_ints = []
    for index in range(100, 201):
        if index < len(lst) and lst[index] < 0:
            negative_ints.append(lst[index])
    return negative_ints
