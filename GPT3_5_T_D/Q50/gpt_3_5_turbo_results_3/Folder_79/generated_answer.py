
def if_contains_anagrams(strings):
    def is_anagram(string1, string2):
        if len(string1) != len(string2):
            return False
        return sorted(string1.lower()) == sorted(string2.lower())
    
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_count += 1
                if anagram_count >= 40:
                    return True
    return False
