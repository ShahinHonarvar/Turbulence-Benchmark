def find_original_set(s1, s2):
    return {i for i in range(min(s1, s2), max(s1, s2) + 1) if s1.issubset(range(i, max(s1, s2) + 1)) and s2.issubset(range(i, max(s1, s2) + 1))}
