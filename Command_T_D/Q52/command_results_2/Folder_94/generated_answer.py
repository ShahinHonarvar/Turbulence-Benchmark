def palindrome_of_length_n(s):
    if not s:
        return set()
    return {p for p in (s[i:j] for i in range(len(s) - 1) for j in range(i + 1, len(s))) if p == p[::-1].lower()}
