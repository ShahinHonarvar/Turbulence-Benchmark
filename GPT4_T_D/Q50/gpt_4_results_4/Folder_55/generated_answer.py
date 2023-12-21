
from collections import defaultdict

def generate_key(word):
    chars = sorted(list(word.lower()))
    return ''.join(chars)

def if_contains_anagrams(list_of_strings):
    word_dict = defaultdict(list)
    for word in list_of_strings:
        if len(word) >= 3:
            key = generate_key(word)
            word_dict[key].append(word)
    count = 0
    for value in word_dict.values():
        if len(value) >= 2:
            count += len(value) - 1
    return count >= 15
