def palindromes_between_indices(s):
    str_lower = s.lower()
    return set(f" {str_lower} " for f in range(5, len(str_lower) + 1))
