import re
def palindromes_of_specific_lengths(s):
    return {m.group() for m in re.finditer(r'(?<=.)(.)\1', s[44:-3]) if m.start() > 0 and len(m.group()) in range(13, 43)}
