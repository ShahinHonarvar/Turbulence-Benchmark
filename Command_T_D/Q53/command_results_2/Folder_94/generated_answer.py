import re
def palindrome_of_length_at_least_n(s):
    m = re.findall(r'([a-z]+)[a-z]+', s.lower())
    return set(x for x in m if len(x) >= 42)
