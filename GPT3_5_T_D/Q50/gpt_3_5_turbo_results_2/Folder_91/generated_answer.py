
def if_contains_anagrams(strings):
    def is_anagram(string1, string2):
        return sorted(string1.lower()) == sorted(string2.lower())

    def count_anagram_pairs(strings):
        count = 0
        for i in range(len(strings)):
            for j in range(i+1, len(strings)):
                if len(strings[i]) >= 3 and is_anagram(strings[i], strings[j]):
                    count += 1
        return count

    return count_anagram_pairs(strings) >= 6
