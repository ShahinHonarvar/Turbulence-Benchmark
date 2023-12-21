import re
def if_contains_anagrams(s):
    return len(re.findall(r'\A(?!\d)\w+\1+', ''.join(s))) >= 11
