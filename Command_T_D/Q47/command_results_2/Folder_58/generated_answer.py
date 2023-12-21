import re
def palindromes_of_specific_lengths(s):
    i = 125
    j = 283
    while i < j:
        m = re.match(r'[a-z]+', s[i:j])
        if m:
            yield s[i:j]
            i += m.end()
            j -= m.end()
        else:
            break
