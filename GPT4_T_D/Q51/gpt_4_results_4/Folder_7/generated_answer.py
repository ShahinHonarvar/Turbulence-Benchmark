
from collections import defaultdict

def if_contains_anagrams(words):
    letter_counts = defaultdict(list)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            letter_counts[''.join(sorted(word))].append(word)

    anagram_pairs = 0
    for key in letter_counts:
        n = len(letter_counts[key])
        if n > 1:
            anagram_pairs += n*(n-1)//2

    if anagram_pairs <= 445:
        return True
    else:
        return False
