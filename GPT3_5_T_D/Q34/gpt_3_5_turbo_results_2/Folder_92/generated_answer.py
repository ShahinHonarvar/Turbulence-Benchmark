
def find_original_set(set1, set2, set3, set4, set5, set6, set7, set8):
    original_set = set()
    for set_arg in [set1, set2, set3, set4, set5, set6, set7, set8]:
        original_set.update(set_arg)
    return original_set
