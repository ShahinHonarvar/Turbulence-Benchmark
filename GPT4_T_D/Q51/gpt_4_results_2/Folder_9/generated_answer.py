
from collections import defaultdict

def if_contains_anagrams(strings):
    def count_anagrams(strings):
        words_by_sorted_chars = defaultdict(list)
        for s in strings:
            words_by_sorted_chars[''.join(sorted(list(s.lower())))].append(s)

        return sum(len(words) * (len(words) - 1) // 2 for words in words_by_sorted_chars.values() if len(words[0]) >= 3)

    return count_anagrams(strings) <= 475
