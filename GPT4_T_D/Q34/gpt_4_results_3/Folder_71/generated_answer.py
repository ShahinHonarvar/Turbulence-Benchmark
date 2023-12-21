
def find_original_set(set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15, set16):
    original_set = set()
    
    all_sets = [set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15, set16]
    
    for s in all_sets:
        original_set = original_set.union(s)
        
    return original_set
