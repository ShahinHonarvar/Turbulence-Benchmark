def palindromes_between_indices(s):
    return {p for i in range(len(s) - 6) for p in (s[i:j] + s[j:i + 6] + s[j:]) if p[::-1] == p}
