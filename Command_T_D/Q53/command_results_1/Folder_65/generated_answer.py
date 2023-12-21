import re
def palindrome_of_length_at_least_n(s):
    if not s:
        return []
    return [i for i in re.findall(r'[A-Z]+\d{4}[A-Z]00\d{4}[A-Z]+', s.lower()) if len(i) >= 15]
