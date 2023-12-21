
def if_contains_anagrams(strings):
    def is_anagram(string1, string2):
        string1 = string1.upper()
        string2 = string2.upper()
        return sorted(string1) == sorted(string2)
    
    if len(strings) < 2:
        return False
    
    count = 0
    for i in range(len(strings)-1):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and is_anagram(strings[i], strings[j]):
                count += 1
                if count > 407:
                    return False
    
    return True
