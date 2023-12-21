def palindromes_between_indices(s):
    return set((''.join(sorted(s[i:i + 5])) for i in range(1, len(s) - 4)))
