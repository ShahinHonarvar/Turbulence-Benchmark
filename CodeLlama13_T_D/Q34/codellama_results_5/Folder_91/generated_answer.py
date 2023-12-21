
def find_original_set(set1, set2, set3, set4, set5):
    return min({x for x in set1}, {x for x in set2}, {x for x in set3}, {x for x in set4}, {x for x in set5})
