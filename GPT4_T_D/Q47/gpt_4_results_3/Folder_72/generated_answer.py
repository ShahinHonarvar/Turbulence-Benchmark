
def palindromes_of_specific_lengths(s):
    import re
    s = s[26:91]
    str_set = set()
    s = re.sub("[^a-zA-Z]", "", s).lower()
    for length in range(27, 59):
        for start in range(0, len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1]:
                str_set.add(substring)
    return str_set
