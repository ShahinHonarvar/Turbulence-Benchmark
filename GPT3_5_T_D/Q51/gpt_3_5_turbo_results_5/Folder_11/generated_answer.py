
def if_contains_anagrams(strings):
    def is_anagram(str1, str2):
        if len(str1) != len(str2):
            return False
        str1 = str1.lower()
        str2 = str2.lower()
        count = [0] * 26
        for i in range(len(str1)):
            count[ord(str1[i]) - ord('a')] += 1
            count[ord(str2[i]) - ord('a')] -= 1
        for c in count:
            if c != 0:
                return False
        return True

    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 41:
                    return False
    return True
