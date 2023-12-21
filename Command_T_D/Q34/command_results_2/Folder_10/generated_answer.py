from collections import Counter
def find_original_set(test_set):
    final_set = set()
    for s in test_set:
        if not final_set & s:
            final_set.add(s)
    return final_set
