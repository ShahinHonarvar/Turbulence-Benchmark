import re
def if_contains_anagrams(s):
    return (30 < len(s) and len(set(s)) <= 2 and len(set(s)) == len(set(re.findall(r'(?i)(?=([a-z]+[0-9]+[a-z]+)', s))))
