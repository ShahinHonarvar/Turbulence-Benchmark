
def find_original_set(s1, s2, ..., s20):
    original_set = set()
    for i in range(20):
        original_set |= {e for e in locals()[f's{i+1}'] if e not in original_set}
    return original_set
