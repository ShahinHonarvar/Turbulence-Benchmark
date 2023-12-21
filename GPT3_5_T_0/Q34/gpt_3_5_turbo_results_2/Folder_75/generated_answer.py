
def find_original_set(set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15):
    original_set = set()
    for s in [set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15]:
        original_set.update(s)
    return original_set
