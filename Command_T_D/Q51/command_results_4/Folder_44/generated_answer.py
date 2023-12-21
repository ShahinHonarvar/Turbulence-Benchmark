import re
def if_contains_anagrams(s):
    return len(re.findall(r'(?i)(?:(?<an1>[a-z]){3})(?<an2>[a-z]){3}', ' '.join(s), flags=re.I)) <= 75
