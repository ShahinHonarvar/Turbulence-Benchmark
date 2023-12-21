
def if_contains_anagrams(strings):
    def is_anagram(str1, str2):
        if len(str1) != len(str2):
            return False
        return sorted(str1.lower()) == sorted(str2.lower())

    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                count += 1
                if count >= 20:
                    return True
    return False
