def palindromes_between_indices(str):
    str = str[4:8]
    return {s[::-1] for s in str.lower() if s == s[::-1]}
