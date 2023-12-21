
def if_contains_anagrams(strings):
    def are_anagrams(str1, str2):
        if len(str1) != len(str2):
            return False
        count = [0] * 26
        for i in range(len(str1)):
            count[ord(str1[i].lower()) - ord('a')] += 1
            count[ord(str2[i].lower()) - ord('a')] -= 1
        for i in range(26):
            if count[i] != 0:
                return False
        return True

    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if are_anagrams(strings[i], strings[j]):
                count += 1
    return count >= 55
