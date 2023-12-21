import re
def if_contains_anagrams(s):
    return len(re.findall(r"(?i)(?=([A-Z]){3}){2})([A-Z]){3}([A-Z]){3}(?!([A-Z]){3}){2}", s)) <= 279
