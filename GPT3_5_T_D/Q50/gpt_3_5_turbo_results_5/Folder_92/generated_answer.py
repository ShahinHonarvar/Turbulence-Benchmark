
def if_contains_anagrams(strings):
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and is_anagram(strings[i], strings[j]):
                anagram_count += 1
                if anagram_count >= 2:
                    return True

    return False
