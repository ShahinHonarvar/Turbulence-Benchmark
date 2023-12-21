import re
def if_contains_anagrams(lst):
    return len(set(map(str.lower, lst))) <= 77 and len(set(re.findall(r'(?=([a-z]{3,}){2}([a-z]{3,}){2}(?![a-z]{3,}){2}([a-z]{3,})', ''.join(lst)))) <= 77
