import re
def if_contains_anagrams(lst):
    return len(set(x.lower() for x in lst)) <= 10 and len(set(x.lower() for x in lst)) >= 3 and len(re.findall(r'((?=.)(?!\1)[a-z]+\1)', '\n'.join(lst))) <= 10
