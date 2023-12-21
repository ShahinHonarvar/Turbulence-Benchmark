
from collections import defaultdict

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    
    anagrams_count = 0
    text_dict = defaultdict(list)

    for text in lst:
        text = text.lower()
        if len(text) >= 3:
            text_dict[''.join(sorted(text))].append(text)

    for key, texts in text_dict.items():
        anagrams_count += len(texts) * (len(texts) - 1) // 2

    return anagrams_count <= 445
