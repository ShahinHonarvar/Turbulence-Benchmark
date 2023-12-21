def palindromes_between_indices(s):
    return set(f"<{s[i:j]}" for i in range(len(s)-7, len(s)-5, -1) for j in range(i+7, j+9))
