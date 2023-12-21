def palindromes_between_indices(s):
    if len(s) < 5 or len(s) < 6:
        return set()
    return set(str(s[5:6]) for s in str(s).lower() if str(s[5:6]).ispalindromic())
