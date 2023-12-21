
from collections import defaultdict

def if_contains_anagrams(l):
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    words = [word for word in l if len(word) >= 3]
    words = [word.lower() for word in words]
    frequency = defaultdict(int)
    
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if is_anagram(words[i], words[j]):
                frequency[words[i]] += 1
                frequency[words[j]] += 1
    
    return sum(val == 2 for val in frequency.values()) <= 38
