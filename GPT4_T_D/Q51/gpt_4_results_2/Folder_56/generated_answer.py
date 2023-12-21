
def if_contains_anagrams(strings):
    from collections import Counter
    sorted_strings = [''.join(sorted(list(word.lower()))) 
                      for word in strings if len(word) >= 3]
    count = Counter(sorted_strings)
    anagram_pairs = sum([v*(v-1)//2 for v in count.values() if v > 1])
    return anagram_pairs <= 11
