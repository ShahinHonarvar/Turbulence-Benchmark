
def if_contains_anagrams(strings):
    def is_anagram(s1, s2):
        if len(s1) != len(s2) or s1.lower() == s2.lower():
            return False
        return sorted(s1.lower()) == sorted(s2.lower())

    count = 0
    for i in range(len(strings)-1):
        for j in range(i+1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                count += 1
            if count >= 77:
                return True
    return False
