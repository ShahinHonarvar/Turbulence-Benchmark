
import collections

def if_contains_anagrams(strings):
    count = 0
    anagrams = collections.defaultdict(int)
    
    for string in strings:
        if len(string) < 3:
            continue
        count += anagrams[string.lower()]
        for i in range(1, len(string)):
            for j in range(len(string) - i + 1):
                sub = ''.join(sorted(string[j:j+i]))
                anagrams[sub] += 1
    
    return count <= 147
