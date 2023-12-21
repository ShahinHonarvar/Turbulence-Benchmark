
def if_contains_anagrams(lst):
    def count_chars(s):
        counts = [0] * 26
        for c in s.lower():
            if c.isalpha():
                counts[ord(c) - ord('a')] += 1
        return counts

    anagram_pairs = 0
    anagrams = {}
    
    for s in lst:
        if len(s) >= 3:
            chars = tuple(count_chars(s))
            if chars in anagrams:
                anagram_pairs += anagrams[chars]
                anagrams[chars] += 1
            else:
                anagrams[chars] = 1
    
    return anagram_pairs >= 246
