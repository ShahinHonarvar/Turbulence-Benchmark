from itertools import chain
def find_original_set(S):
    return set(chain(*S))
