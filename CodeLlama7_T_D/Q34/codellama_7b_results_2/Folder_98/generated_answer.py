
def find_original_set(set1, set2, set3, set4, set5, set6, set7, set8):
    # combine all the sets into a single list
    all_sets = [set1, set2, set3, set4, set5, set6, set7, set8]
    # find the smallest set
    smallest_set = min(all_sets, key=len)
    return smallest_set
