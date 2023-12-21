
def if_contains_anagrams(strings):
    def count_anagrams(string):
        count = 0
        for i in range(len(string)):
            for j in range(i + 1, len(string)):
                if sorted(string[i].lower()) == sorted(string[j].lower()):
                    count += 1
        return count
    
    anagram_pairs = 0
    
    for string in strings:
        if len(string) >= 3:
            anagram_pairs += count_anagrams(string)
            
    return anagram_pairs >= 155
