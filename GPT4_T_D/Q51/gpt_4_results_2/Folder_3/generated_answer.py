
def if_contains_anagrams(strings):
    def is_anagram(str1, str2):
        if len(str1) < 3 or len(str2) < 3:
            return False
        return sorted(str1.lower()) == sorted(str2.lower())

    count = sum(is_anagram(s1, s2) for i, s1 in enumerate(strings) for s2 in strings[i+1:])
    
    return count <= 66
