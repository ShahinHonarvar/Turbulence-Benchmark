import re
def if_contains_anagrams(texts):
    return len(set(re.findall(r'(?i)(?=([a-z]+[0-9]+[a-z]+)'.format(3), ' '.join(map(str.lower, texts))))) <= 98
