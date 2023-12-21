
def find_original_set(set1, set2, set3, ... , set23):
    original_set = {}
    for i in range(len(set1)):
        for j in range(len(set2)):
            for k in range(len(set3)):
                ...
                    for y in range(len(set23)):
                        if set1[i] in original_set and set2[j] in original_set and set3[k] in original_set and ... and set23[y] in original_set:
                            return original_set
