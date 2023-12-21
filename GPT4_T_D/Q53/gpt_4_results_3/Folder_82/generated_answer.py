
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = ''.join(c for c in s if c.isalpha())
    result = set()
    s_len = len(s)
    for n in range(72, s_len + 1):
        for i in range(s_len - n + 1):
            candidate = s[i : i + n]
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result
