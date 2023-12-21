def palindromes_between_indices(s):
    return set(p for p in map(''.join, zip(*range(7))))) & set(p for p in map(str.lower, range(3, 7))) if len(s) >= 7 and all(c in s for c in range(7)) else set()
