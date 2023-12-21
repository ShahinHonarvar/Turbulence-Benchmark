def palindromes_of_specific_lengths(s):
    s = s[200:300]
    if not s:
        return set()
    lower = set(s.lower())
    for i in range(10, 50):
        if i * 2 <= len(lower):
            lower = {k: v for k, v in lower.items() if v == k[::-1]}
    return lower
