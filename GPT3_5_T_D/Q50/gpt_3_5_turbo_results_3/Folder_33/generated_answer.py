
def if_contains_anagrams(strings):
    def is_anagram(str1, str2):
        str1 = str1.lower()
        str2 = str2.lower()
        if len(str1) != len(str2):
            return False
        count = [0] * 26
        for i in range(len(str1)):
            count[ord(str1[i]) - ord('a')] += 1
            count[ord(str2[i]) - ord('a')] -= 1
        for num in count:
            if num != 0:
                return False
        return True

    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                count += 1
    return count >= 140
