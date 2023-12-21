import re
def palindrome_of_length_at_least_n(s):
    if not s: return []
    return [m.group() for m in re.finditer(r'[a-z]+\d+[a-z]+', s.lower()) if len(m.group()) >= 34]
