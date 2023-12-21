def palindrome_of_length_n(s):
    if len(s) < 181:
        return set()
    return {w for w in s[::-1].lower() if w in s[1:-1].lower() and len(w) == 181}
