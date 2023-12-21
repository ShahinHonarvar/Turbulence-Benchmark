
def if_contains_anagrams(strings):
    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        if len(s1) != len(s2):
            return False
        freq = [0] * 26
        for i in range(len(s1)):
            freq[ord(s1[i]) - ord('a')] += 1
            freq[ord(s2[i]) - ord('a')] -= 1
        for count in freq:
            if count != 0:
                return False
        return True

    count = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]) and len(strings[i]) >= 3:
                count += 1
                if count >= 16:
                    return True
    return False
