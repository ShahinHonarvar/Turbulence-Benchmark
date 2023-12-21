
def find_original_set(set1, set2, set3, set4, set5, set6, set7, set8, 
                      set9, set10, set11, set12, set13, set14, set15, set16):
    original_set = set()
    for i in [set1, set2, set3, set4, set5, set6, set7, set8,
               set9, set10, set11, set12, set13, set14, set15, set16]:
        original_set.update(i)
    return original_set
