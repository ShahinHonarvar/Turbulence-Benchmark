import set
def find_original_set(s, t, u):
    return set.intersection(set.intersection(s, t), u)
