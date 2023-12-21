 
def if_contains_anagrams(strings):
    def count_anagrams(string):
        counts = {}
        for char in string:
            char = char.lower()
            counts[char] = counts.get(char, 0) + 1
        return counts
    
    anagram_pairs = 0
    string_counts = {}
    
    for string in strings:
        count = count_anagrams(string)
        if len(string) >= 3:
            if count in string_counts:
                anagram_pairs += string_counts[count]
                string_counts[count] += 1
            else:
                string_counts[count] = 1
    
    return anagram_pairs >= 85
