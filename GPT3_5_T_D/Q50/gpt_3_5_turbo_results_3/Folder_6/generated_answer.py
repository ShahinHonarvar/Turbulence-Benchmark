
def if_contains_anagrams(strings):
    def is_anagram(string1, string2):
        return sorted(string1.lower()) == sorted(string2.lower())

    def count_anagrams(string, strings):
        count = 0
        for other in strings:
            if len(other) >= 3 and is_anagram(string, other):
                count += 1
        return count

    anagram_pairs = 0
    for i in range(len(strings)):
        anagram_pairs += count_anagrams(strings[i], strings[i+1:])

    return anagram_pairs >= 26
