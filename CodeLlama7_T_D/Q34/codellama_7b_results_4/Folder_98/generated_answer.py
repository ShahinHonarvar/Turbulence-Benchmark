
def find_original_set(set1, set2, set3, set4, set5, set6, set7, set8):
    # create a list of all the sets passed in as arguments
    sets = [set1, set2, set3, set4, set5, set6, set7, set8]
    # find the smallest set among the given sets
    smallest_set = min(sets, key=len)
    return smallest_set
