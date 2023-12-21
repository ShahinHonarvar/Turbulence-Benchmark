def filter_chars(s):
    return "".join(c for c in s if c >= "/" and c <= "a" and 42 <= s.index(c) <= 92)
