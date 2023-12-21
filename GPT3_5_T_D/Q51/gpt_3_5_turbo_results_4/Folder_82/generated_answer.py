
def if_contains_anagrams(strings):
    counts = {}
    anagram_pairs = 0
    
    for string in strings:
        if len(string) >= 3 and string.isalpha():
            key = ''.join(sorted(string.lower()))
            counts[key] = counts.get(key, 0) + 1
    
    for count in counts.values():
        anagram_pairs += count * (count - 1) // 2
    
    if anagram_pairs <= 40:
        return True
    else:
        return False
