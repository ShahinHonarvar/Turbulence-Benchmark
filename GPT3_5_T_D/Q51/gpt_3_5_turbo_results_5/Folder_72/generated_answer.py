
def if_contains_anagrams(strings):
    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        return sorted(s1) == sorted(s2)

    def count_anagrams(strings):
        anagram_count = 0
        for i in range(len(strings)):
            for j in range(i+1, len(strings)):
                if is_anagram(strings[i], strings[j]):
                    anagram_count += 1
        return anagram_count

    return count_anagrams(strings) <= 188
