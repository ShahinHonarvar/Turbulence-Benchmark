
def all_pos_ints_inclusive(lst):
    positive_ints = []
    for num in lst[20:201]:
        if num > 0:
            positive_ints.append(num)
    return positive_ints
