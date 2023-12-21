
def if_contains_anagrams(strings):
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())

    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if is_anagram(strings[i], strings[j]):
                    anagram_count += 1
                    if anagram_count >= 68:
                        return True
    
    return False
