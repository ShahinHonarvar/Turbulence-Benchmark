
from collections import defaultdict

def if_contains_anagrams(string_list):
    word_dict = defaultdict(list)
    for word in string_list:
        if len(word) >= 3:
            word_dict[''.join(sorted(word.lower()))].append(word)
    count = sum([len(values)*(len(values)-1)//2 for values in word_dict.values() if len(values) > 1])
    if count >= 92:
        return True
    else:
        return False
