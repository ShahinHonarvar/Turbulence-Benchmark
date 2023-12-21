def find_original_set(S):
    return set(min(s for s in (set(S), set(range(len(S))))) for S in zip(*S))
