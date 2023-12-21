
def if_contains_anagrams(strings):
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    pairs = 0
    for i in range(len(strings)-1):
        for j in range(i+1, len(strings)):
            if len(strings[i]) < 3 or len(strings[j]) < 3:
                continue
            if is_anagram(strings[i], strings[j]):
                pairs += 1
                if pairs >= 6:
                    return True
    return False
