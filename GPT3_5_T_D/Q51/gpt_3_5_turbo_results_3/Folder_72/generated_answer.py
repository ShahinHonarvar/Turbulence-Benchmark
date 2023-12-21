
from collections import Counter

def if_contains_anagrams(strings):
    # Filter out strings that have fewer than three characters
    strings = [s.lower() for s in strings if len(s) >= 3]

    # Count the frequency of each character in each string
    counts = [Counter(s) for s in strings]

    # Count the number of unique anagram pairs
    anagram_pairs = 0
    for i in range(len(counts)):
        for j in range(i + 1, len(counts)):
            if counts[i] == counts[j]:
                anagram_pairs += 1

    return anagram_pairs <= 188
