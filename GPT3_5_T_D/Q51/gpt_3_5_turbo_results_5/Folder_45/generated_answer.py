
def if_contains_anagrams(strings):
    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        if len(s1) != len(s2):
            return False
        for c in s1:
            if c not in s2:
                return False
            s2 = s2.replace(c, '', 1)
        return True

    count = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                count += 1
            if count > 464:
                return False
    return True
