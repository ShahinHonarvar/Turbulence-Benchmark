
def if_contains_anagrams(strings):
    def is_anagram(str1, str2):
        str1 = str1.lower()
        str2 = str2.lower()
        if len(str1) != len(str2):
            return False
        return sorted(str1) == sorted(str2)

    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_count += 1
                if anagram_count > 38:
                    return False
    return True
