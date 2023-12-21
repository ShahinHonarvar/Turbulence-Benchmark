
def if_contains_anagrams(strings):
    def is_anagram(string1, string2):
        return sorted(string1.lower()) == sorted(string2.lower())
    
    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and is_anagram(strings[i], strings[j]):
                count += 1
                if count > 89:
                    return False
    return True
