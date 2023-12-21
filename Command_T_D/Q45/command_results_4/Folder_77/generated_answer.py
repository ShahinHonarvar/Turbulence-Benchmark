def palindromes_between_indices(str):
    return set((''.join(c for c in str[4:6] if c in str.lower()) for _ in range(1, len(str) + 1 - 4)))
