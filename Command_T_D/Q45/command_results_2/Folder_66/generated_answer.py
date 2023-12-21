def palindromes_between_indices(s):
    return set(i[::-1] for i in range(5, len(s) + 1) if s[i-5:i+6].lower() == i[::-1])
