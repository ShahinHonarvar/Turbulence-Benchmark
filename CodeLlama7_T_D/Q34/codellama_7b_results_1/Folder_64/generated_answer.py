
def find_original_set(set1, set2, set3, set4, set5, set6):
    # Find the smallest set that contains all the given sets
    smallest_set = None
    for i in range(1, 7):
        if len(set1) <= len(set2) and len(set1) <= len(set3) and len(set1) <= len(set4) and len(set1) <= len(set5) and len(set1) <= len(set6):
            smallest_set = set1
        elif len(set2) <= len(set1) and len(set2) <= len(set3) and len(set2) <= len(set4) and len(set2) <= len(set5) and len(set2) <= len(set6):
            smallest_set = set2
        elif len(set3) <= len(set1) and len(set3) <= len(set2) and len(set3) <= len(set4) and len(set3) <= len(set5) and len(set3) <= len(set6):
            smallest_set = set3
        elif len(set4) <= len(set1) and len(set4) <= len(set2) and len(set4) <= len(set3) and len(set4) <= len(set5) and len(set4) <= len(set6):
            smallest_set = set4
        elif len(set5) <= len(set1) and len(set5) <= len(set2) and len(set5) <= len(set3) and len(set5) <= len(set4) and len(set5) <= len(set6):
            smallest_set = set5
        elif len(set6) <= len(set1) and len(set6) <= len(set2) and len(set6) <= len(set3) and len(set6) <= len(set4) and len(set6) <= len(set5):
            smallest_set = set6
    return smallest_set
