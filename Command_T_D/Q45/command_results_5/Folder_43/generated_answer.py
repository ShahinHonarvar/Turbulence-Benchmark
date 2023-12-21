def palindromes_between_indices(s):
    return set(f"({s[2:5].lower()})" for i in range(2, len(s) - 5))
