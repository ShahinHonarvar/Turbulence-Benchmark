
from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    hash_table = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = "".join(sorted(word))
            if sorted_word in hash_table:
                hash_table[sorted_word].append(word)
            else:
                hash_table[sorted_word] = [word]
    for value in hash_table.values():
        n = len(value)
        count += n * (n-1) // 2
    if count > 58:
        return True
    else:
        return False
