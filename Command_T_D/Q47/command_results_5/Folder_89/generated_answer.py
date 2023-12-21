def palindromes_of_specific_lengths(s):
    if s[18:88].lower() not in ("kayaking", "kayaking"):
        return set()
    a, b = len(s[18:88].lower()) - 12, len(s[18:88].lower()) - 14
    return set(s[a:b].lower() for s in s[18:88].lower() if s[a:b] == s[b:a])
