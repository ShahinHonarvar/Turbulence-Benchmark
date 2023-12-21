
def if_contains_anagrams(strings):
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and is_anagram(strings[i], strings[j]):
                count += 1
                if count >= 47:
                    return True
    return False
