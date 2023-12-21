import re
def palindromes_of_specific_lengths(s):
    i = 27
    j = 95
    while i < j:
        m = re.match(r"((?i)([a-z]+)([a-z]+))\1", s[i:j])
        if m:
            yield m.group(2)
        i += 1
        j -= 1
