import re
def if_contains_anagrams(s):
    return (len(s) * len(s)) <= 39 and len(set(s)) <= 39 and len(re.findall(r'(?i)(?=([^aieou])\1)', ' '.join(s))) <= 39
