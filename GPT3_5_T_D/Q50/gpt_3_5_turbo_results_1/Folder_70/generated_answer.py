
def if_contains_anagrams(string_list):
    def is_anagram(string1, string2):
        if len(string1) != len(string2):
            return False
        
        return sorted(string1.lower()) == sorted(string2.lower())

    count = 0
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            if is_anagram(string_list[i], string_list[j]):
                count += 1
                if count >= 189:
                    return True
    
    return False
