def palindrome_of_length_at_least_n(s):
    import re
    return {m.group() for m in re.finditer(r'[a-z]+', s, flags=re.I)}
