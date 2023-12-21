
def find_original_set(set1, set2):
    return min((set1 | set2), key=len)
