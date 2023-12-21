
def if_contains_anagrams(strings):
    def is_anagram(str1, str2):
        if len(str1) == len(str2):
            return sorted(str1.lower()) == sorted(str2.lower())
        else:
            return False
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_count += 1
                if anagram_count >= 20:
                    return True
    return False
